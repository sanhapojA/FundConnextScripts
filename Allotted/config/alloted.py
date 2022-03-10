from config.read_text import *
from config.database import *

# For fundcode type switch in.
in_transaction_code = ['SWI']

class UnitHolderID:

    def __init__(self, uhid, new_uhid):
        self.uhid = uhid
        self.new_uhid = new_uhid

    def findUnitDummy(self, column):
        try:
            find_unit_dummy = database.query(
                """
                SELECT
                    NewUnitholderIDReferenceNo, UnitholderIDReferenceNo
                FROM
                    FCN_CustomerProfile
                WHERE
                    NewUnitholderIDReferenceNo = '""" + self.new_uhid + """'
                """
            )
            for row in find_unit_dummy:
                return row[column]

        except Exception as e:
            return e

    def unitholderID(self):
        try:
            if self.uhid == 'SEG' or self.uhid == 'OMN':
                unitholder_id = self.findUnitDummy(1)

            else:
                unitholder_id = self.uhid

            return str(unitholder_id)

        except Exception as e:
            return e


class SwitchFund:
    
    def __init__(self):
        self.fund_code = ''
        self.counter_fundCode = ''

    def change_fund_code(self):
        return self.counter_fundCode

    def change_counter_fund_code(self):
        return self.fund_code

    def set_fund_code(self, fundCode):
        self.fund_code = fundCode

    def set_counter_fund_code(self, counterFundCode):
        self.counter_fundCode = counterFundCode


class StatusFund:

    def __init__(self, transactionCode, effectiveDate):
        self.transaction_code = transactionCode
        self.effective_date = effectiveDate

    def status(self):
        if self.transaction_code in in_transaction_code and self.effective_date != file_date:
            status = 'WAITING'
        elif self.transaction_code in in_transaction_code and self.effective_date == file_date:
            status = 'ALLOTTED'
        else:
            status = 'ALLOTTED'
        return status


class Holiday:
    pass


class EffectiveDateFund():

    def __init__(self, transactionCode, effectiveDate):
        self.transaction_code = transactionCode
        self.effective_date = effectiveDate

    def effective(self):
        if (self.transaction_code in in_transaction_code) and self.effective_date != file_date:
            effective_date = 'T+3'

        elif (self.transaction_code in in_transaction_code) and self.effective_date == file_date:
            effective_date = self.effective_date

        else:
            effective_date = self.effective_date

        return effective_date


class AllottedFund():
    def __init__(self, fundCode, transactionCode, effectiveDate):
        self.fund_code = fundCode
        self.transaction_code = transactionCode
        self.effective_date = effectiveDate
        self.amount = ''
        self.unit = ''

    def nav(self):
        '''
        nav[1] = (NAV)
        nav[2] = (OfferNAV)
        nav[3] = (BidNAV)
        nav[4] = (SwitchOutNAV)
        nav[5] = (SwitchInNAV)
        '''
        try:
            nav = database.query(
                """
                    SELECT FundCode, NAV, OfferNAV, BidNAV, SwitchOutNAV, SwitchInNAV, NAVDate
                    FROM FCN_NAV
                    WHERE FundCode = '""" + self.fund_code + """' AND NAVDate = '""" + self.effective_date + """'
                    """
            )
            
            for n in nav:
                return n

        except:
            pass

    def allotted_nav(self):

        nav = self.nav()

        try:
            if (self.transaction_code in in_transaction_code) and self.effective_date == file_date:
                allot_nav = str(nav[5])

            elif self.transaction_code == 'SWO':
                allot_nav = str(nav[4])

            elif self.transaction_code == 'RED':
                allot_nav = str(nav[3])

            elif self.transaction_code == 'SUB':
                allot_nav = str(nav[2])

            else:
                allot_nav = ''

            return allot_nav

        except:
            pass

    def allotted_date(self):
        try:
            if self.effective_date == file_date:
                allotted_date = self.effective_date
            else:
                allotted_date = ''
            return allotted_date
        
        except:
            pass

    def get_amount(self, amount):
        try:
            self.amount = amount
        except:
            pass

    def get_unit(self, unit):
        try:
            self.unit = unit
        except:
            pass

    def allotted_unit(self):
        try:
            # Subscription Bath
            if (self.transaction_code == 'SUB' or self.transaction_code in in_transaction_code) and self.effective_date == file_date:
                allotted_unit = str(float(self.amount) /
                                    float(self.allotted_nav())).split('.')
                allotted_unit = str(allotted_unit[0] + '.' + allotted_unit[1][0:4])

            # Reedemtion Unit
            elif (self.transaction_code == 'RED' or self.transaction_code == 'SWO') and self.amount == '':
                allotted_unit = str(self.unit)

            # Reedemtion Bath
            elif (self.transaction_code == 'RED' or self.transaction_code == 'SWO') and self.unit == '':
                allotted_unit = str(float(self.amount) /
                                    float(self.allotted_nav())).split('.')
                allotted_unit = allotted_unit[0] + '.' + allotted_unit[1][0:4]

            else:
                allotted_unit = ''

            return allotted_unit
        
        except:
            pass

    def allotted_amount(self):
        try:
            # Subscription Bath
            if (self.transaction_code == 'SUB' or self.transaction_code in in_transaction_code) and self.effective_date == file_date:
                allotted_amount = f'{float(self.allotted_unit()) * float(self.allotted_nav()):.2f}'

            # Reedemtion Unit
            elif self.transaction_code == 'RED' or self.transaction_code == 'SWO' and self.amount == '':
                allotted_amount = f'{float(self.allotted_unit()) * float(self.allotted_nav()):.2f}'

            # Reedemtion Bath
            elif self.transaction_code == 'RED' or self.transaction_code == 'SWO' and self.unit == '':
                allotted_amount = f'{float(self.amount):.2f}'

            else:
                allotted_amount = ''

            return allotted_amount
        
        except:
            pass

    def fund_fee(self):
        try:
            select_fee = database.query(
                """
                    SELECT FundCode ,FrontFeeActivate, FrontEndFee, BackFeeActivate, BackEndFee, WithholdingTax, VAT
                    FROM FCN_Fee
                    WHERE FundCode = '""" + self.fund_code + """'
                    """
            )
            
            for f in select_fee:
                FrontFeeActivate = f[1]
                FrontEndFee = f[2]
                BackFeeActivate = f[3]
                BackEndFee = f[4]
                WithholdingTax = f[5]
                VAT = f[6]
            
            if (self.transaction_code == 'SUB' or self.transaction_code in in_transaction_code) and FrontFeeActivate == 'Y' and self.effective_date == file_date:
                return {
                    'wht': WithholdingTax,
                    'vat': VAT
                    }

            elif (self.transaction_code == 'SUB' or self.transaction_code in in_transaction_code) and FrontFeeActivate == 'N' and self.effective_date == file_date:
                return {
                    'wht': f'{0:.2f}', 
                    'vat': f'{0:.2f}'
                    }
 
            elif (self.transaction_code == 'RED' or self.transaction_code == 'SWO') and BackFeeActivate == 'Y' and self.effective_date == file_date:
                return {
                    'wht': WithholdingTax,
                    'vat': VAT
                    }

            elif (self.transaction_code == 'RED' or self.transaction_code == 'SWO') and BackFeeActivate == 'N' and self.effective_date == file_date:
                return {
                    'wht': f'{0:.2f}',
                    'vat': f'{0:.2f}'
                    }

            else:
                return {
                    'wht': f'{0:.2f}',
                    'vat': f'{0:.2f}',
                    }

        except:
            pass
         
    def cost(self):

        nav = self.nav()

        try:
            tx_cost = '{:.2f}'.format(float(self.allotted_unit()) * float(nav[1]))
            fee_include_vat = '{:.2f}'.format(float(self.allotted_amount()) - float(tx_cost))
        except:
            fee_include_vat = f'{0:.2f}'

        return str(fee_include_vat)
    
    def fee(self):

        try:
            if self.vat() != '0.00':
                fee_excluding_vat = '{:.2f}'.format(float(self.cost()) - float(self.vat()))
            else:
                fee_excluding_vat = '0.00'
        except:
            fee_excluding_vat = '0.00'

        return str(fee_excluding_vat)

    def witholding_tax(self):

        try:
            withholdingTax = '{:.2f}'.format(float(self.fund_fee()['wht']/100) * float(self.fee()))
        except:
            withholdingTax = '0.00'

        return str(withholdingTax)

    def vat(self):

        try:
            vat = '{:.2f}'.format(float(self.cost()) * float(self.fund_fee()['vat']) / (100 + float(self.fund_fee()['vat'])))
        except:
            vat = '0.00'

        return str(vat)
