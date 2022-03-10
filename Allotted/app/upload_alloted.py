from config.database import *
from config.read_text import *
from datetime import datetime


def convertDate(strDate):
    date = strDate
    if date != '':
        dt = datetime.strptime(date, '%Y%m%d%H%M%S').strftime(
            '%Y-%m-%dT%H:%M:%S')
    else:
        date = '19000101000000'
        dt = datetime.strptime(date, '%Y%m%d%H%M%S').strftime(
            '%Y-%m-%dT%H:%M:%S')
    return dt


def convertNumeric(strNumeric):
    numeric = strNumeric
    if numeric != '':
        numeric = strNumeric
    else:
        numeric = 0
    return str(numeric)


def checkDuplicate(sacode, uhid, fund_code, tran_id, as_of_date):
    chk_duplicate = database.query(
        """
        SELECT SACode, UnitholderID, FundCode, TransactionID, AsOfDate
        FROM FCN_AllotedTransactions
        WHERE SACode = '""" + sacode + """' AND 
        UnitholderID = '""" + uhid + """' AND
        FundCode = '""" + fund_code + """' AND
        TransactionID = '""" + tran_id + """' AND 
        AsOfDate = '""" + as_of_date + """'
        """
    )
    for row in chk_duplicate:
        SACode = row[0]
        UnitholderID = row[1]
        FundCode = row[2]
        TransactionID = row[3]
        AsOfDate = str(row[4]).replace('-', '')
        return SACode + UnitholderID + FundCode + TransactionID + AsOfDate


for row in range(len(file_allotted)):
    SAOrderReferenceNo = file_allotted[row][0]
    TransactionDateTime = convertDate(file_allotted[row][1])
    SACode = file_allotted[row][3]
    UnitholderID = file_allotted[row][4]
    NewUnitholderReferenceNo = file_allotted[row][5]
    TransactionCode = file_allotted[row][6]
    FundCode = file_allotted[row][7]
    RedemptionType = file_allotted[row][10]
    Amount = convertNumeric(file_allotted[row][11])
    Unit = convertNumeric(file_allotted[row][12])
    EffectiveDate = file_allotted[row][13]
    CounterFundCode = file_allotted[row][14]
    PaymentType = file_allotted[row][16]
    BankCode = file_allotted[row][17]
    BankAccountCreditCardNumber = file_allotted[row][18]
    ChequeNo = file_allotted[row][19]
    ChequeDate = file_allotted[row][20]
    ICLicense = file_allotted[row][21]
    BranchNo = file_allotted[row][22]
    Channel = file_allotted[row][23]
    ForceEntry = file_allotted[row][24]
    LTFCondition = file_allotted[row][25]
    ReasontosellLTFRMF = file_allotted[row][26]
    RMFCapitalgainwithholdingtaxchoice = file_allotted[row][27]
    RMFCapitalamountredeemchoice = file_allotted[row][28]
    Autoredeemfundcode = file_allotted[row][29]
    TransactionID = file_allotted[row][30]
    Status = file_allotted[row][31]
    AMCOrderReferenceNo = file_allotted[row][32]
    AllotmentDate = file_allotted[row][33]
    AllottedNAV = convertNumeric(file_allotted[row][34])
    AllottedAmount = convertNumeric(file_allotted[row][35])
    AllotedUnit = convertNumeric(file_allotted[row][36])
    Fee = convertNumeric(file_allotted[row][37])
    WithholdingTax = convertNumeric(file_allotted[row][38])
    VAT = convertNumeric(file_allotted[row][39])
    Brokeragefee = convertNumeric(file_allotted[row][40])
    WithholdingTaxforLTFRMF = convertNumeric(file_allotted[row][41])
    AMCPayDate = file_allotted[row][42]
    RegistrarTransactionFlag = file_allotted[row][43]
    Sellallunitflag = file_allotted[row][44]
    SettlementBankCode = file_allotted[row][45]
    SettlementBankAccount = file_allotted[row][46]
    RejectReason = file_allotted[row][47]
    CHQBranch = file_allotted[row][48]
    TaxInvoiceNo = file_allotted[row][49]
    AMCSwitchingOrderReferenceNo = file_allotted[row][50]
    BrokeragefeeVAT = convertNumeric(file_allotted[row][52])
    ApprovalCode = file_allotted[row][53]
    NAVDate = file_allotted[row][54]
    Creditcardissuer = file_allotted[row][56]
    InvestorPaymentInstructor = file_allotted[row][57]
    InvestorPaymentStatus = file_allotted[row][58]
    FundSettlementFlag = file_allotted[row][59]
    FinNetProcessingType = file_allotted[row][60]
    InvestorPaymentStartDateTime = convertDate(file_allotted[row][61])
    InvestorPaymentEndDateTime = convertDate(file_allotted[row][62])
    InvestorPaymentResultCode = file_allotted[row][63]
    InvestorBankCode = file_allotted[row][64]
    InvestorBankAccount = file_allotted[row][65]
    SABankCode = file_allotted[row][66]
    SABankAccount = file_allotted[row][67]
    AMCBankCode = file_allotted[row][68]
    AMCBankAccount = file_allotted[row][69]
    SASettlementBankCode = file_allotted[row][70]
    SASettlementBankAccount = file_allotted[row][71]
    AMCSettlementBankCode = file_allotted[row][72]
    AMCSettlementBankAccount = file_allotted[row][73]
    FundSettlementStartDateTime = convertDate(file_allotted[row][74])
    FundSettlementEndDateTime = convertDate(file_allotted[row][75])
    FundSettlementResultCode = file_allotted[row][76]
    Custodianbankcode = file_allotted[row][77]
    CustodianbankAccount = file_allotted[row][78]
    CustodianpaymentStartDateTime = convertDate(file_allotted[row][79])
    CustodianpaymentEndDateTime = convertDate(file_allotted[row][80])
    Custodianpaymentresultcode = file_allotted[row][81]
    AsOfDate = file_date

    compareTextAlloted = SACode + UnitholderID + FundCode + TransactionID + AsOfDate
    compareSQLAlloted = checkDuplicate(
        SACode, UnitholderID, FundCode, TransactionID, AsOfDate)

    # ตรวจสอบการ Upload text file ซ้ำแต่ละวัน โดยเปรียบเทียบกันระหว่าง Text File กับ SQL
    # ถ้าไม่่มีใน SQL จะทำการ Upload text file ถ้าซ้ำจะขึ้น Duplicate
    if compareTextAlloted != compareSQLAlloted:

        database.commit(
            """
                INSERT INTO FCN_AllotedTransactions
                (
                    SAOrderReferenceNo, TransactionDateTime, SACode, UnitholderID, NewUnitholderReferenceNo, TransactionCode, 
                    FundCode, RedemptionType, Amount, Unit, EffectiveDate, CounterFundCode, PaymentType, BankCode, 
                    BankAccountCreditCardNumber, ChequeNo, ChequeDate, ICLicense, BranchNo, Channel, ForceEntry, 
                    LTFCondition, ReasonToSellLTFRMF, RMFCapitalGainWithholdingTaxChoice, RMFCapitalAmountRedeemChoice, 
                    AutoRedeemFundCode, TransactionID, Status, AMCOrderReferenceNo, AllotmentDate, AllottedNAV, AllottedAmount, 
                    AllotedUnit, Fee, WithholdingTax, VAT, BrokerageFee, WithholdingTaxForLTFRMF, AMCPayDate, 
                    RegistrarTransactionFlag, SellAllUnitFlag, SettlementBankCode, SettlementBankAccount, RejectReason, 
                    CHQBranch, TaxInvoiceNo, AMCSwitchingOrderReferenceNo, BrokerageFeeVAT, ApprovalCode, NAVDate, 
                    CreditCardIssuer, InvestorPaymentInstructor, InvestorPaymentStatus, FundSettlementFlag, 
                    FinNetProcessingType, InvestorPaymentStartDateTime, InvestorPaymentEndDateTime, 
                    InvestorPaymentResultCode, InvestorBankCode, InvestorBankAccount, SABankCode, SABankAccount, 
                    AMCBankCode, AMCBankAccount, SASettlementBankCode, SASettlementBankAccount, AMCSettlementBankCode, 
                    AMCSettlementBankAccount, FundSettlementStartDateTime, FundSettlementEndDateTime, 
                    FundSettlementResultCode, CustodianBankCode, CustodianBankAccount, CustodianPaymentStartDateTime, 
                    CustodianPaymentEndDateTime, CustodianPaymentResultCode, AsOfDate
                )

                VALUES
                (
                    '""" + SAOrderReferenceNo + """', '""" + TransactionDateTime + """', '""" + SACode + """', 
                    '""" + UnitholderID + """', '""" + NewUnitholderReferenceNo + """', '""" + TransactionCode + """', 
                    '""" + FundCode + """', '""" + RedemptionType + """', '""" + Amount + """', '""" + Unit + """', 
                    '""" + EffectiveDate + """', '""" + CounterFundCode + """', '""" + PaymentType + """', '""" + BankCode + """', 
                    '""" + BankAccountCreditCardNumber + """', '""" + ChequeNo + """', '""" + ChequeDate + """', 
                    '""" + ICLicense + """', '""" + BranchNo + """', '""" + Channel + """', '""" + ForceEntry + """', 
                    '""" + LTFCondition + """', '""" + ReasontosellLTFRMF + """', '""" + RMFCapitalgainwithholdingtaxchoice + """', 
                    '""" + RMFCapitalamountredeemchoice + """', '""" + Autoredeemfundcode + """', '""" + TransactionID + """', 
                    '""" + Status + """', '""" + AMCOrderReferenceNo + """', '""" + AllotmentDate + """', 
                    '""" + AllottedNAV + """', '""" + AllottedAmount + """', '""" + AllotedUnit + """', 
                    '""" + Fee + """', '""" + WithholdingTax + """', '""" + VAT + """', '""" + Brokeragefee + """', 
                    '""" + WithholdingTaxforLTFRMF + """', '""" + AMCPayDate + """', '""" + RegistrarTransactionFlag + """', 
                    '""" + Sellallunitflag + """', '""" + SettlementBankCode + """', '""" + SettlementBankAccount + """', 
                    '""" + RejectReason + """', '""" + CHQBranch + """', '""" + TaxInvoiceNo + """', 
                    '""" + AMCSwitchingOrderReferenceNo + """', '""" + BrokeragefeeVAT + """', '""" + ApprovalCode + """', 
                    '""" + NAVDate + """', '""" + Creditcardissuer + """', '""" + InvestorPaymentInstructor + """', 
                    '""" + InvestorPaymentStatus + """', '""" + FundSettlementFlag + """', '""" + FinNetProcessingType + """', 
                    '""" + InvestorPaymentStartDateTime + """', '""" + InvestorPaymentEndDateTime + """', 
                    '""" + InvestorPaymentResultCode + """', '""" + InvestorBankCode + """', '""" + InvestorBankAccount + """', 
                    '""" + SABankCode + """', '""" + SABankAccount + """', '""" + AMCBankCode + """', 
                    '""" + AMCBankAccount + """', '""" + SASettlementBankCode + """', '""" + SASettlementBankAccount + """', 
                    '""" + AMCSettlementBankCode + """', '""" + AMCSettlementBankAccount + """', 
                    '""" + FundSettlementStartDateTime + """', '""" + FundSettlementEndDateTime + """', 
                    '""" + FundSettlementResultCode + """', '""" + Custodianbankcode + """', '""" + CustodianbankAccount + """', 
                    '""" + CustodianpaymentStartDateTime + """', '""" + CustodianpaymentEndDateTime + """', 
                    '""" + Custodianpaymentresultcode + """', '""" + AsOfDate + """'
                )
                """
        )

        print('Upload Success: {}'.format(SACode + '|' + UnitholderID +
              '|' + FundCode + '|' + TransactionID + '|' + AsOfDate))

    else:
        print('Duplicate: {}'.format(SACode + '|' + UnitholderID +
              '|' + FundCode + '|' + TransactionID + '|' + AsOfDate))
