from config.read_text import *
from config.database import *
from config.alloted import *
import os


def make_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Create Disrectory. ' + directory)


def bankAccount(uhid):
    try:
        bank_account = database.query(
        """
        SELECT BankCode, BankAccount FROM FCN_BankAccount
        WHERE UnitholderIDReferenceNo = '"""+ uhid +"""'
        """
        )
        for acc in bank_account:
            return acc
        
    except:
        pass


#-- Create folder.
make_folder(path_folder_allotted)


with open(path_file_allotted, 'w', encoding='utf-8') as f:

    #FundConnext head format.
    f.write('{0}|XSpringAM|{1}|V3.0\n'.format(dateToday, total_line_transaction))

    for row in range(len(file_paidtransaction)):
        Filler = ''
        SAOrderReferenceNo = file_paidtransaction[row][0]
        TransactionDateTime = file_paidtransaction[row][1]
        SACode = file_paidtransaction[row][3]

        UnitholderID = file_paidtransaction[row][4]
        NewUnitholderReferenceNo = file_paidtransaction[row][5]
        UnitholderID = UnitHolderID(UnitholderID, NewUnitholderReferenceNo)
        UnitholderID = UnitholderID.unitholderID()

        TransactionCode = file_paidtransaction[row][6]
        FundCode = file_paidtransaction[row][7]
        RedemptionType = file_paidtransaction[row][10]
        Amount = file_paidtransaction[row][11]
        Unit = file_paidtransaction[row][12]

        EffectiveDate = file_paidtransaction[row][13]
        EffectiveDate = EffectiveDateFund(TransactionCode, EffectiveDate).effective()

        CounterFundCode = file_paidtransaction[row][14]
        PaymentType = file_paidtransaction[row][16]
        BankCode = file_paidtransaction[row][17]
        BankAccountCreditCardNumber = file_paidtransaction[row][18]
        ChequeNo = file_paidtransaction[row][19]
        ChequeDate = file_paidtransaction[row][20]
        ICLicense = file_paidtransaction[row][21]
        BranchNo = file_paidtransaction[row][22]
        Channel = file_paidtransaction[row][23]
        ForceEntry = file_paidtransaction[row][24]
        LTFCondition = file_paidtransaction[row][25]
        ReasontosellLTFRMF = file_paidtransaction[row][26]
        RMFCapitalgainwithholdingtaxchoice = file_paidtransaction[row][27]
        RMFCapitalamountredeemchoice = file_paidtransaction[row][28]
        Autoredeemfundcode = file_paidtransaction[row][29]
        TransactionID = file_paidtransaction[row][30]
        Status = StatusFund(TransactionCode, EffectiveDate).status()
        AMCOrderReferenceNo = 'XAM' + TransactionID

        allotted_fund = AllottedFund(FundCode, TransactionCode, EffectiveDate)
        allotted_fund.get_amount(Amount)
        allotted_fund.get_unit(Unit)

        AllotmentDate = allotted_fund.allotted_date()
        AllottedNAV = allotted_fund.allotted_nav()
        AllottedAmount = allotted_fund.allotted_amount()
        AllotedUnit = allotted_fund.allotted_unit()

        Fee = allotted_fund.fee()
        WithholdingTax = allotted_fund.witholding_tax()
        VAT = allotted_fund.vat()

        Brokeragefee = file_paidtransaction[row][40]
        WithholdingTaxforLTFRMF = file_paidtransaction[row][41]
        AMCPayDate = file_paidtransaction[row][42]
        RegistrarTransactionFlag = file_paidtransaction[row][43]
        Sellallunitflag = file_paidtransaction[row][44]


        SettlementBankCode = file_paidtransaction[row][45]
        if (TransactionCode in ['RED', 'SUB'] and PaymentType[3:] == '_SA') and SettlementBankCode != '':
            SettlementBankCode = SettlementBankCode
        elif (TransactionCode in ['RED', 'SUB'] and PaymentType[3:] == '_SA') and SettlementBankCode == '':
            SettlementBankCode = bankAccount(UnitholderID)[0]
        else:
            SettlementBankCode = ''


        SettlementBankAccount = file_paidtransaction[row][46]
        if (TransactionCode in ['RED', 'SUB'] and PaymentType[-3:] == '_SA') and SettlementBankAccount != '':
            SettlementBankAccount = SettlementBankAccount
        elif (TransactionCode in ['RED', 'SUB'] and PaymentType[-3:] == '_SA') and SettlementBankAccount == '':
            SettlementBankAccount = bankAccount(UnitholderID)[1]
        else:
            SettlementBankAccount = ''


        RejectReason = file_paidtransaction[row][47]
        CHQBranch = file_paidtransaction[row][48]
        TaxInvoiceNo = file_paidtransaction[row][49]
        AMCSwitchingOrderReferenceNo = file_paidtransaction[row][50]
        BrokeragefeeVAT = file_paidtransaction[row][52]
        ApprovalCode = file_paidtransaction[row][53]
        NAVDate = file_paidtransaction[row][54]
        Creditcardissuer = file_paidtransaction[row][56]
        InvestorPaymentInstructor = file_paidtransaction[row][57]
        InvestorPaymentStatus = file_paidtransaction[row][58]
        FundSettlementFlag = file_paidtransaction[row][59]
        FinNetProcessingType = file_paidtransaction[row][60]
        InvestorPaymentStartDateTime = file_paidtransaction[row][61]
        InvestorPaymentEndDateTime = file_paidtransaction[row][62]
        InvestorPaymentResultCode = file_paidtransaction[row][63]
        InvestorBankCode = file_paidtransaction[row][64]
        InvestorBankAccount = file_paidtransaction[row][65]
        SABankCode = file_paidtransaction[row][66]
        SABankAccount = file_paidtransaction[row][67]
        AMCBankCode = file_paidtransaction[row][68]
        AMCBankAccount = file_paidtransaction[row][69]
        SASettlementBankCode = file_paidtransaction[row][70]
        SASettlementBankAccount = file_paidtransaction[row][71]
        AMCSettlementBankCode = file_paidtransaction[row][72]
        AMCSettlementBankAccount = file_paidtransaction[row][73]
        FundSettlementStartDateTime = file_paidtransaction[row][74]
        FundSettlementEndDateTime = file_paidtransaction[row][75]
        FundSettlementResultCode = file_paidtransaction[row][76]
        Custodianbankcode = file_paidtransaction[row][77]
        CustodianbankAccount = file_paidtransaction[row][78]
        CustodianpaymentStartDateTime = file_paidtransaction[row][79]
        CustodianpaymentEndDateTime = file_paidtransaction[row][80]
        Custodianpaymentresultcode = file_paidtransaction[row][81]

        Filler_Row83_to_Row150 = ''
        for _ in range(0, 66):
            Filler_Row83_to_Row150 += '|'


        def print_allotted():
            print(SAOrderReferenceNo + '|' + TransactionDateTime + '|' + Filler + '|' + SACode + '|' + UnitholderID + '|' + NewUnitholderReferenceNo + '|' +
                TransactionCode + '|' + FundCode + '|' + Filler + '|' + Filler + '|' + RedemptionType + '|' + Amount + '|' + Unit + '|' + EffectiveDate + '|' +
                CounterFundCode + '|' + Filler + '|' + PaymentType + '|' + BankCode + '|' + BankAccountCreditCardNumber + '|' + ChequeNo + '|' + ChequeDate + '|' +
                ICLicense + '|' + BranchNo + '|' + Channel + '|' + ForceEntry + '|' + LTFCondition + '|' + ReasontosellLTFRMF + '|' +
                RMFCapitalgainwithholdingtaxchoice + '|' + RMFCapitalamountredeemchoice + '|' + Autoredeemfundcode + '|' + TransactionID + '|' +
                Status + '|' + AMCOrderReferenceNo + '|' + AllotmentDate + '|' + AllottedNAV + '|' + AllottedAmount + '|' + AllotedUnit + '|' +
                Fee + '|' + WithholdingTax + '|' + VAT + '|' + Brokeragefee + '|' + WithholdingTaxforLTFRMF + '|' + AMCPayDate + '|' +
                RegistrarTransactionFlag + '|' + Sellallunitflag + '|' + SettlementBankCode + '|' + SettlementBankAccount + '|' + RejectReason + '|' +
                CHQBranch + '|' + TaxInvoiceNo + '|' + AMCSwitchingOrderReferenceNo + '|' + Filler + '|' + BrokeragefeeVAT + '|' + ApprovalCode + '|' +
                NAVDate + '|' + Filler + '|' + Creditcardissuer + '|' + InvestorPaymentInstructor + '|' + InvestorPaymentStatus + '|' + FundSettlementFlag + '|' +
                FinNetProcessingType + '|' + InvestorPaymentStartDateTime + '|' + InvestorPaymentEndDateTime + '|' + InvestorPaymentResultCode + '|' +
                InvestorBankCode + '|' + InvestorBankAccount + '|' + SABankCode + '|' + SABankAccount + '|' + AMCBankCode + '|' + AMCBankAccount + '|' +
                SASettlementBankCode + '|' + SASettlementBankAccount + '|' + AMCSettlementBankCode + '|' + AMCSettlementBankAccount + '|' +
                FundSettlementStartDateTime + '|' + FundSettlementEndDateTime + '|' + FundSettlementResultCode + '|' + Custodianbankcode + '|' +
                CustodianbankAccount + '|' + CustodianpaymentStartDateTime + '|' + CustodianpaymentEndDateTime + '|' + Custodianpaymentresultcode + '|' + '|' + 
                Filler_Row83_to_Row150, file=f)


        # Subscription.
        if TransactionCode == 'SUB':
            print_allotted()
        
        # Reedemtion.
        elif TransactionCode == 'RED':
            print_allotted()

        # Switching In.
        elif TransactionCode in in_transaction_code:
            print_allotted()

        # Switching.
        elif TransactionCode == 'SWT':

            switch_transaction_code = ['SWO', 'SWI']
            for sw in range(len(switch_transaction_code)):

                # Change TransactionCode SWT --> SWO and SWI.
                TransactionCode = switch_transaction_code[sw]

                # SWI.
                if TransactionCode == 'SWI':
                    EffectiveDate = ''
                    EffectiveDate = EffectiveDateFund(TransactionCode, EffectiveDate).effective()
                    
                    sf = SwitchFund()
                    sf.set_fund_code(FundCode)
                    sf.set_counter_fund_code(CounterFundCode)
                    FundCode = sf.change_fund_code()
                    CounterFundCode = sf.change_counter_fund_code()

                    RedemptionType = 'AMT'
                    Amount = allotted_fund.allotted_amount()
                    Unit = ''

                Status = StatusFund(TransactionCode, EffectiveDate).status()

                # Allotted SWI & SWO.
                allotted_fund = AllottedFund(FundCode, TransactionCode, EffectiveDate)
                allotted_fund.get_amount(Amount)
                allotted_fund.get_unit(Unit)
                AllotmentDate = allotted_fund.allotted_date()
                AllottedNAV = allotted_fund.allotted_nav()
                AllottedAmount = allotted_fund.allotted_amount()
                AllotedUnit = allotted_fund.allotted_unit()

                Fee = allotted_fund.fee()
                
                print_allotted()
        
        else:
            pass
    
    print("Success !!!")