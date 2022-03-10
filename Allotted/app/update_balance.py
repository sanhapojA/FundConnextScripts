from config.database import *
from config.read_text import *
from config.alloted import *
from datetime import datetime


def convertNumeric(strNumeric):
    numeric = strNumeric
    if numeric != '':
        numeric = strNumeric
    else:
        numeric = 0
    return str(numeric)


def checkFundCode(uhid, fund_code):
    checkFundCode = database.query(
        """
        SELECT UnitholderID, FundCode
        FROM FCN_UnitholderBalance
        WHERE UnitholderID = '""" + uhid + """' AND FundCode = '""" + fund_code + """'
        """
    )
    for row in checkFundCode:
        UnitholderID = row[0]
        FundCode = row[1]
        return 'Unitholder: {0}, Fund Code: {1}'.format(UnitholderID, FundCode)


def insertBalance(
        sa_code, uhid, fund_code, u_balance, amount, available_balance, available_amount, pending_balance,
        pending_amount, pledge_unit, avg_cost, inv_year, allow_redeem_year, allow_sell_flag, nav, nav_date):
    database.commit(
        """
            INSERT INTO FCN_UnitholderBalance
            (
                SACode, UnitholderID, FundCode, UnitBalance, Amount, AvailableUnitBalance, AvailableAmount, PendingUnitBalance, 
                PendingAmount, PledgeUnit, AverageCost, InvestmentYear, AllowRedeemYear, AllowSellFlag, NAV, NAVDate
            )

            VALUES
            (
                """ + sa_code + """', """ + uhid + """', """ + fund_code + """', """ + u_balance + """',
                """ + amount + """', """ + available_balance + """', """ + available_amount + """', """ + pending_balance + """', 
                """ + pending_amount + """', """ + pledge_unit + """', """ + avg_cost + """', """ + inv_year + """', 
                """ + allow_redeem_year + """', """ + allow_sell_flag + """', """ + nav + """', """ + nav_date + """'
            )
            """
    )


def deleteBalance(sa_code, uhid, fund_code):
    database.commit(
        """
        DELETE FCN_UnitholderBalance
        WHERE """ + sa_code + """' AND """ + uhid + """' AND """ + fund_code + """'
        """
    )


def foundBalance(sa_code, uhid, fund_code, column):
    foundBalance = database.query(
        """
        SELECT SACode, UnitholderID, FundCode, UnitBalance, Amount, CostValue, AverageCost
        FROM FCN_UnitholderBalance
        WHERE SACode = '""" + sa_code + """' AND UnitholderID = '""" + uhid + """' AND FundCode = '""" + fund_code + """'
        """
    )
    for row in foundBalance:
        return row[column]


def convertUnit(unitBlance):
    varUnitBlance = str(unitBlance).split('.')
    strUnitBlance = varUnitBlance[0] + '.' + varUnitBlance[1][0:4]
    return strUnitBlance


def convertAmount(amountBlance):
    strAmountBlance = '{:.2f}'.format(amountBlance)
    return strAmountBlance


def dateFile():
    dateFile = file_date
    dateFile = datetime.strptime(dateFile, '%Y%m%d')
    dateFile = dateFile.strftime('%Y-%m-%d %H:%M:%S.%f')
    return dateFile[:-3]


def updateBalance():
    for row in range(len(file_allotted)):

        global vartxtAsOfDate

        vartxtSACode = file_allotted[row][3]
        vartxtUnitholderID = file_allotted[row][4]
        vartxtTransactionCode = file_allotted[row][6]
        vartxtFundCode = file_allotted[row][7]
        vartxtAmount = convertNumeric(file_allotted[row][11])
        vartxtAllottedNAV = convertNumeric(file_allotted[row][34])
        file_allottedUnit = convertNumeric(file_allotted[row][36])
        vartxtAsOfDate = dateFile()
        vartxtStatus = file_allotted[row][31]

        # ต้องเป็นสถานะ ALLOTTED แล้วเท่านั้นจึงดำเนินการจัดการกับ Balance
        if vartxtStatus == 'ALLOTTED':

            # ทำการตรวจสอบว่าเคยซื้อกองทุนเดิมหรือกองทุนใหม่จาก DB:Fundconnext_PRD, TB:FCN_UnitholderBalance
            varCheckFundCode = checkFundCode(
                vartxtUnitholderID, vartxtFundCode)

            def nav():
                nav = AllottedFund(vartxtFundCode, vartxtTransactionCode, vartxtAsOfDate).nav()  # Date:AsOfDate
                return str(nav[1])

            def unit(transaction):

                unit = foundBalance(vartxtSACode, vartxtUnitholderID, vartxtFundCode, 3)

                if transaction == 'SUB' and varCheckFundCode == None:
                    unitBalance = file_allottedUnit

                elif transaction == 'SUB' and varCheckFundCode != None:
                    floatUnitBalance = float(unit) + float(file_allottedUnit)
                    floatUnitBalance = round(floatUnitBalance, 4)
                    unitBalance = convertUnit(floatUnitBalance)

                elif transaction == 'RED':
                    floatUnitBalance = float(unit) - float(file_allottedUnit)
                    floatUnitBalance = round(floatUnitBalance, 4)
                    unitBalance = convertUnit(floatUnitBalance)

                else:
                    pass

                return unitBalance

            def amount(varUnit):
                amount = float(varUnit) * float(nav())
                return convertAmount(amount)

            def costValue(transaction):

                _costValue = foundBalance(
                    vartxtSACode, vartxtUnitholderID, vartxtFundCode, 5)

                if transaction == 'SUB' and varCheckFundCode == None:
                    cost = vartxtAmount

                elif transaction == 'SUB' and varCheckFundCode != None:
                    floatCostValue = float(_costValue) + float(vartxtAmount)
                    cost = convertAmount(floatCostValue)

                elif transaction == 'RED':
                    floatCostValue = float(
                        unit(transaction)) * float(avgCost(transaction))
                    cost = convertAmount(floatCostValue)

                else:
                    pass

                return cost

            def avgCost(transaction):

                _avgCost = foundBalance(
                    vartxtSACode, vartxtUnitholderID, vartxtFundCode, 6)

                if transaction == 'SUB' and varCheckFundCode == None:
                    averageCost = vartxtAllottedNAV

                elif transaction == 'SUB' and varCheckFundCode != None:
                    floatAverageCost = float(
                        costValue(transaction)) / float(unit(transaction))
                    averageCost = convertUnit(floatAverageCost)

                elif transaction == 'RED':
                    averageCost = str(_avgCost)

                else:
                    pass

                return averageCost

            varUnit = unit(vartxtTransactionCode)
            varAmount = amount(varUnit)
            varAvailableBalance = varUnit
            varAvailableAmount = varAmount
            varPendingunitBalance = '0'
            varPendingAmount = '0'
            varPledgeunit = '0'
            varAverageCost = avgCost(vartxtTransactionCode)
            varInvestmentYear = ''
            varAllowRedeemYear = ''
            varAllowSellFlag = ''
            varNAVDate = vartxtAsOfDate
            varCostValues = costValue(vartxtTransactionCode)
            varNAV = nav()

            # กรณี "ไม่ซื้อ" กองเดิมจะทำการ Upload Balance
            if varCheckFundCode == None:

                database.commit(
                    """
                    INSERT INTO FCN_UnitholderBalance
                    (
                        SACode, UnitholderID, FundCode, UnitBalance, Amount, AvailableUnitBalance, AvailableAmount, 
                        PendingUnitBalance, PendingAmount, PledgeUnit, AverageCost, CostValue, InvestmentYear, AllowRedeemYear, 
                        AllowSellFlag, NAV, NAVDate
                    )

                    VALUES
                    (
                        '""" + vartxtSACode + """', '""" + vartxtUnitholderID + """', '""" + vartxtFundCode + """', '""" + varUnit + """', 
                        '""" + varAmount + """', '""" + varAvailableBalance + """', '""" + varAvailableAmount + """', 
                        '""" + varPendingunitBalance + """', '""" + varPendingAmount + """', '""" + varPledgeunit + """', 
                        '""" + varAverageCost + """', '""" + varCostValues + """', '""" + varInvestmentYear + """', '""" + varAllowRedeemYear + """', 
                        '""" + varAllowSellFlag + """', '""" + varNAV + """', '""" + varNAVDate + """'
                    )
                    """
                )

                print(
                    'INSERT :' + '|' +
                    vartxtSACode + '|' + vartxtUnitholderID + '|' + vartxtFundCode + '|' + varUnit + '|' +
                    varAmount + '|' + varAvailableBalance + '|' + varAvailableAmount + '|' +
                    varPendingunitBalance + '|' + varPendingAmount + '|' + varPledgeunit + '|' +
                    varAverageCost + '|' + varCostValues + '|' + varInvestmentYear + '|' +
                    varAllowRedeemYear + '|' + varAllowSellFlag + '|' + varNAV + '|' + varNAVDate
                )

            # กรณี "ซื้อ" กองเดิมจะทำการ Update Balance
            else:

                database.commit(
                    """
                        UPDATE FCN_UnitholderBalance

                        SET UnitBalance = '""" + varUnit + """', Amount = '""" + varAmount + """',
                        AvailableUnitBalance = '""" + varAvailableBalance + """', AvailableAmount = '""" + varAvailableAmount + """',
                        PendingUnitBalance = '""" + varPendingunitBalance + """', PendingAmount = '""" + varPendingAmount + """',
                        PledgeUnit = '""" + varPledgeunit + """', AverageCost = '""" + varAverageCost + """',
                        CostValue = '""" + varCostValues + """', InvestmentYear = '""" + varInvestmentYear + """',
                        AllowRedeemYear = '""" + varAllowRedeemYear + """', AllowSellFlag = '""" + varAllowSellFlag + """',
                        NAV = '""" + varNAV + """', NAVDate = '""" + varNAVDate + """'

                        WHERE SACode = '""" + vartxtSACode + """' AND UnitholderID = '""" + vartxtUnitholderID + """' AND
                        FundCode = '""" + vartxtFundCode + """'
                        """
                )

                print(
                    'UPDATE :' + '|' +
                    vartxtSACode + '|' + vartxtUnitholderID + '|' + vartxtFundCode + '|' + varUnit + '|' +
                    varAmount + '|' + varAvailableBalance + '|' + varAvailableAmount + '|' +
                    varPendingunitBalance + '|' + varPendingAmount + '|' + varPledgeunit + '|' +
                    varAverageCost + '|' + varCostValues + '|' + varInvestmentYear + '|' +
                    varAllowRedeemYear + '|' + varAllowSellFlag + '|' + varNAV + '|' + varNAVDate
                )

        # สถานะอื่นที่ไม่ใช่ ALLOTTED จะ Pass ไป
        else:
            print('Status: {}, UniholderID: {}, FundCode: {}'.format(vartxtStatus, vartxtUnitholderID, vartxtFundCode))


def updateAllBalance():

    database.commit(
        """
            UPDATE 
                FCN_UnitholderBalance 
            SET 
                FCN_UnitholderBalance.NAV = FCN_NAV.NAV, 
                FCN_UnitholderBalance.NAVDate = FCN_NAV.NAVDate, 
                FCN_UnitholderBalance.Amount = ROUND(FCN_UnitholderBalance.UnitBalance * FCN_NAV.NAV, 2), 
                FCN_UnitholderBalance.AvailableAmount = ROUND(FCN_UnitholderBalance.UnitBalance * FCN_NAV.NAV, 2) 
            FROM 
                FCN_UnitholderBalance 
            INNER JOIN FCN_NAV ON (
                FCN_UnitholderBalance.FundCode = FCN_NAV.FundCode
            ) 
            WHERE 
                FCN_NAV.FundCode = FCN_UnitholderBalance.FundCode 
                AND FCN_NAV.NAVDate = '""" + dateFile() + """'
            """
       )


# Execution Functions
updateBalance()
updateAllBalance()