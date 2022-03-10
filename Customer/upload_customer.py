from module_read_text import read_text
from datetime import datetime, date
from module_customer import *
from module_connect_database import SQL

# date = '20211229'

date = datetime.today()
date = date.strftime('%Y%m%d')

# read text customer.txt
file_new_customer = r'P:/FundConnext/FundConnext-PRD/Download Files/' + date + '/' + date + '_XSpringAM_NEWACCOUNT/' + date + '_XSpringAM_CUSTOMER.txt'
text = read_text(1, file_new_customer)

# connect database
database = SQL('Fundconnext_PRD', '192.168.100.5', 'sa', 'EnSEC$999')


def ReplaceText(value):
    return str(value).replace("'", "''")


def customer_profile():
    for i in range(len(text)):
        TransactionFlag = text[i][0]
        NewUnitholderIDReferenceNo = text[i][1]
        AccountType = text[i][2]
        UnitLinkAccountFlag = text[i][3]
        SACode = text[i][4]
        InvestorType = text[i][5]
        Sequence = text[i][6]
        Jointaccountcondition = text[i][7]
        accountholdername = text[i][8]
        TitleTH = text[i][9]
        TitleEN = text[i][10]
        FirstNameTH = text[i][11]
        LastNameTH = text[i][12]
        FirstNameEN = text[i][13]
        LastNameEN = text[i][14]
        IDType = text[i][15]
        PassportCountry = text[i][16]
        JusristicType = text[i][17]
        JuristicTypeOtherDesc = text[i][18]
        TaxExemption = text[i][19]
        OperatingInThailand = text[i][20]
        IDNo = text[i][21]
        IDExpiryDate = text[i][22]
        IDExpiryDateFlag = text[i][23]
        BirthDate = text[i][24]
        NationalityRegisterCountry = text[i][25]
        MarriedStatus = text[i][26]
        Email = text[i][27]
        Mobile = text[i][28]
        Phone = text[i][29]
        Fax = text[i][30]
        SpouseFirstNameTH = text[i][31]
        SpouseLastNameTH = text[i][32]
        SpouseFirstNameEN = text[i][33]
        SpouseLastNameEN = text[i][34]
        OccupationID = text[i][85]
        OccupationDesc = text[i][86]
        BusinessTypeID = text[i][87]
        BusinessTypeDesc = text[i][88]
        IncomeID = text[i][89]
        IncomeSourceCountry = text[i][90]
        IncomeTypeCode = text[i][91]
        IncomeSourceDesc = text[i][92]
        PoliticianFlag = text[i][93]
        PoliticalPosition = text[i][94]
        SuitabilityTestDate = text[i][95]
        RiskProfileLevel = text[i][96]
        FXRiskFlag = text[i][97]
        FuturesRiskFlag = text[i][98]
        FATCATestDate = text[i][99]
        FATCAFlag = text[i][100]
        TotalIncomeperYear = text[i][101]
        JuristicAuthorizedSignatory = text[i][102]
        TransactionCondition = text[i][103]
        TaxID = text[i][104]
        TaxBranch = text[i][105]
        MailingMethod = text[i][106]
        InvestmentObjective = text[i][107]
        InvestmentObjectiveOther = text[i][108]
        ICLicense = text[i][109]
        BranchNo = text[i][110]
        FundGroup = text[i][111]
        NDIDFlag = text[i][112]
        NDIDRequestID = text[i][113]
        AssetValue = text[i][114]
        ShareholderEquity = text[i][115]
        OpenChannel = text[i][116]
        AsOfDate = dateFile(file_new_customer)

        if TransactionFlag == 'U':
            UnitholderID = NewUnitholderIDReferenceNo
        else:
            UnitholderID = UHID(IDNo, AsOfDate)
            UnitholderID = UnitholderID.unitholder_id()

        database.insert(
            """
                INSERT INTO FCN_CustomerProfile
                (
                    TransactionFlag, NewUnitholderIDReferenceNo, UnitholderIDReferenceNo, AccountType, UnitLinkAccountFlag,
                    SACode, InvestorType, Sequence, JointAccountCondition, AccountHolderName, TitleTH, TitleEN, FirstNameTH,
                    LastNameTH, FirstNameEN, LastNameEN, IDType, PassportCountry, JusristicType, JuristicTypeOtherDesc,
                    TaxExemption, OperatingInThailand, IDNo, IDExpiryDate, IDExpiryDateFlag, BirthDate, NationalityRegisterCountry,
                    MarriedStatus, Email, Mobile, Phone, Fax, SpouseFirstNameTH, SpouseLastNameTH, SpouseFirstNameEN,
                    SpouseLastNameEN, OccupationID, OccupationDesc, BusinessTypeID, BusinessTypeDesc, IncomeID, IncomeSourceCountry,
                    IncomeTypeCode, IncomeSourceDesc, PoliticianFlag, PoliticalPosition, SuitabilityTestDate, RiskProfileLevel,
                    FXRiskFlag, FuturesRiskFlag, FATCATestDate, FATCAFlag, TotalIncomePerYear,
                    JuristicAuthorizedSignatory, TransactionCondition, TaxID, TaxBranch, MailingMethod, InvestmentObjective,
                    InvestmentObjectiveOther, ICLicense, BranchNo, FundGroup, NDIDFlag, NDIDRequestID, AssetValue, ShareholderEquity,
                    OpenChannel, AsOfDate
                )

                VALUES
                (
                    '""" + TransactionFlag + """', '""" + NewUnitholderIDReferenceNo + """', '""" + UnitholderID + """',
                    '""" + AccountType + """', '""" + UnitLinkAccountFlag + """', '""" + SACode + """', '""" + InvestorType + """',
                    '""" + Sequence + """', '""" + Jointaccountcondition + """', '""" + accountholdername + """',
                    '""" + TitleTH + """', '""" + TitleEN + """', '""" + FirstNameTH + """', '""" + LastNameTH + """',
                    '""" + FirstNameEN + """', '""" + LastNameEN + """', '""" + IDType + """', '""" + PassportCountry + """',
                    '""" + JusristicType + """', '""" + JuristicTypeOtherDesc + """', '""" + TaxExemption + """',
                    '""" + OperatingInThailand + """', '""" + IDNo + """', '""" + IDExpiryDate + """', '""" + IDExpiryDateFlag + """',
                    '""" + BirthDate + """', '""" + NationalityRegisterCountry + """', '""" + MarriedStatus + """',
                    '""" + Email + """', '""" + Mobile + """', '""" + Phone + """', '""" + Fax + """', '""" + SpouseFirstNameTH + """',
                    '""" + SpouseLastNameTH + """', '""" + SpouseFirstNameEN + """', '""" + SpouseLastNameEN + """',
                    '""" + OccupationID + """', '""" + OccupationDesc + """', '""" + BusinessTypeID + """', '""" + BusinessTypeDesc + """',
                    '""" + IncomeID + """', '""" + IncomeSourceCountry + """', '""" + IncomeTypeCode + """', '""" + IncomeSourceDesc + """',
                    '""" + PoliticianFlag + """', '""" + PoliticalPosition + """', '""" + SuitabilityTestDate + """',
                    '""" + RiskProfileLevel + """', '""" + FXRiskFlag + """', '""" + FuturesRiskFlag + """', '""" + FATCATestDate + """',
                    '""" + FATCAFlag + """', '""" + TotalIncomeperYear + """', '""" + JuristicAuthorizedSignatory + """',
                    '""" + TransactionCondition + """', '""" + TaxID + """', '""" + TaxBranch + """', '""" + MailingMethod + """',
                    '""" + InvestmentObjective + """', '""" + InvestmentObjectiveOther + """', '""" + ICLicense + """',
                    '""" + BranchNo + """', '""" + FundGroup + """', '""" + NDIDFlag + """', '""" + NDIDRequestID + """',
                    '""" + AssetValue + """', '""" + ShareholderEquity + """', '""" + OpenChannel + """', '""" + AsOfDate + """'
                )
            """
        )

        print(
            'CustomerProfile - Upload UHID: {0}, Name: {1}'.format(UnitholderID, FirstNameTH))


def customer_profile_address():
    for i in range(len(text)):
        TransactionFlag = text[i][0]
        NewUnitholderIDReferenceNo = text[i][1]
        IDNo = text[i][21]
        IdentificationDocumentAddressNo = text[i][35]
        IdentificationDocumentMoo = text[i][36]
        IdentificationDocumentPlace = text[i][37]
        IdentificationDocumentRoomNo = text[i][38]
        IdentificationDocumentFloor = text[i][39]
        IdentificationDocumentSoi = text[i][40]
        IdentificationDocumentRoad = text[i][41]
        IdentificationDocumentTambon = text[i][42]
        IdentificationDocumentAmphur = text[i][43]
        IdentificationDocumentProvince = text[i][44]
        IdentificationDocumentPostalCode = text[i][45]
        IdentificationDocumentCountry = text[i][46]
        IdentificationDocumentPhone = text[i][117]
        WorkplaceName = text[i][47]
        WorkAddressNo = text[i][48]
        WorkMoo = text[i][49]
        WorkPlace = text[i][50]
        WorkRoomNo = text[i][51]
        WorkFloor = text[i][52]
        WorkSoi = text[i][53]
        WorkRoad = text[i][54]
        WorkTambon = text[i][55]
        WorkAmphur = text[i][56]
        WorkProvince = text[i][57]
        WorkPostalCode = text[i][58]
        WorkCountry = text[i][59]
        WorkPosition = text[i][60]
        CurrentAddressNo = text[i][61]
        CurrentMoo = text[i][62]
        CurrentPlace = text[i][63]
        CurrentRoomNo = text[i][64]
        CurrentFloor = text[i][65]
        CurrentSoi = text[i][66]
        CurrentRoad = text[i][67]
        CurrentTambon = text[i][68]
        CurrentAmphur = text[i][69]
        CurrentProvince = text[i][70]
        CurrentPostalCode = text[i][71]
        CurrentCountry = text[i][72]
        MailingAddressNo = text[i][73]
        MailingMoo = text[i][74]
        MailingPlace = text[i][75]
        MailingRoomNo = text[i][76]
        MailingFloor = text[i][77]
        MailingSoi = text[i][78]
        MailingRoad = text[i][79]
        MailingTambon = text[i][80]
        MailingAmphur = text[i][81]
        MailingProvince = text[i][82]
        MailingPostalCode = text[i][83]
        MailingCountry = text[i][84]
        AsOfDate = dateFile(file_new_customer)

        if TransactionFlag == 'U':
            UnitholderID = NewUnitholderIDReferenceNo
        else:
            UnitholderID = UHID(IDNo, AsOfDate)
            UnitholderID = UnitholderID.unitholder_id()

        database.insert(
            """
            INSERT FCN_CustomerProfileAddress
            (
                TransactionFlag, NewUnitholderIDReferenceNo, UnitholderIDReferenceNo, IdentificationDocumentAddressNo,
                IdentificationDocumentMoo, IdentificationDocumentPlace, IdentificationDocumentRoomNo, IdentificationDocumentFloor,
                IdentificationDocumentSoi, IdentificationDocumentRoad, IdentificationDocumentTambon, IdentificationDocumentAmphur,
                IdentificationDocumentProvince, IdentificationDocumentPostalCode, IdentificationDocumentCountry, IdentificationDocumentPhone,
                WorkplaceName, WorkAddressNo, WorkMoo, WorkPlace, WorkRoomNo, WorkFloor, WorkSoi, WorkRoad, WorkTambon, WorkAmphur,
                WorkProvince, WorkPostalCode, WorkCountry, WorkPosition, CurrentAddressNo, CurrentMoo, CurrentPlace, CurrentRoomNo,
                CurrentFloor, CurrentSoi, CurrentRoad, CurrentTambon, CurrentAmphur, CurrentProvince, CurrentPostalCode, CurrentCountry,
                MailingAddressNo, MailingMoo, MailingPlace, MailingRoomNo, MailingFloor, MailingSoi, MailingRoad, MailingTambon,
                MailingAmphur, MailingProvince, MailingPostalCode, MailingCountry, AsOfDate
            )

            VALUES
            (
                '""" + TransactionFlag + """', '""" + NewUnitholderIDReferenceNo + """', '""" + UnitholderID + """',
                '""" + IdentificationDocumentAddressNo + """', '""" + IdentificationDocumentMoo + """',
                '""" + IdentificationDocumentPlace + """', '""" + IdentificationDocumentRoomNo + """',
                '""" + IdentificationDocumentFloor + """', '""" + IdentificationDocumentSoi + """', '""" + IdentificationDocumentRoad + """',
                '""" + IdentificationDocumentTambon + """', '""" + IdentificationDocumentAmphur + """',
                '""" + IdentificationDocumentProvince + """', '""" + IdentificationDocumentPostalCode + """',
                '""" + IdentificationDocumentCountry + """', '""" + IdentificationDocumentPhone + """', '""" + WorkplaceName + """',
                '""" + WorkAddressNo + """', '""" + WorkMoo + """', '""" + WorkPlace + """', '""" + WorkRoomNo + """', '""" + WorkFloor + """',
                '""" + WorkSoi + """', '""" + WorkRoad + """', '""" + WorkTambon + """', '""" + WorkAmphur + """', '""" + WorkProvince + """',
                '""" + WorkPostalCode + """', '""" + WorkCountry + """', '""" + WorkPosition + """', '""" + CurrentAddressNo + """',
                '""" + CurrentMoo + """', '""" + CurrentPlace + """', '""" + CurrentRoomNo + """', '""" + CurrentFloor + """',
                '""" + CurrentSoi + """', '""" + CurrentRoad + """', '""" + CurrentTambon + """', '""" + CurrentAmphur + """',
                '""" + CurrentProvince + """', '""" + CurrentPostalCode + """', '""" + CurrentCountry + """', '""" + MailingAddressNo + """',
                '""" + MailingMoo + """', '""" + MailingPlace + """', '""" + MailingRoomNo + """', '""" + MailingFloor + """',
                '""" + MailingSoi + """', '""" + MailingRoad + """', '""" + MailingTambon + """', '""" + MailingAmphur + """',
                '""" + MailingProvince + """', '""" + MailingPostalCode + """', '""" + MailingCountry + """', '""" + AsOfDate + """'
            )

            """
        )

        print('CustomerProfileAddress - Upload UHID: {0}'.format(UnitholderID))


customer_profile()
customer_profile_address()
