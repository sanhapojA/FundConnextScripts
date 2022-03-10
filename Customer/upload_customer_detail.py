from module_read_text import read_text
from datetime import datetime, date
from module_connect_database import SQL
from module_customer import *

# date = '20210917'

date = datetime.today()
date = date.strftime('%Y%m%d')

# read text customer.txt
file_customer_detail = r'P:/FundConnext/FundConnext-PRD/Download Files/' + date + '/' + date + '_XSpringAM_NEWACCOUNT/' + date + '_XSpringAM_CUSTOMER_DETAIL.txt'
text = read_text(1, file_customer_detail)

# connect database
database = SQL('Fundconnext_PRD', '192.168.100.5', 'sa', 'EnSEC$999')


def customer_profile_detail():
    for i in range(len(text)):
  
        NewUnitholderIDReferenceNo = text[i][0]
        
        def unitholder_id(newUhid):
            unitHolder = database.query(
            """
            SELECT NewUnitholderIDReferenceNo, UnitholderIDReferenceNo
            FROM FCN_CustomerProfile
            WHERE NewUnitholderIDReferenceNo = '"""+ newUhid +"""'
            """
            )
            for row in unitHolder:
                return row[1]
                
        UnitholderID = unitholder_id(NewUnitholderIDReferenceNo)

        Type = text[i][1]
        Sequence = text[i][2]
        ParentReferenceID = text[i][3]
        FirstNameTH = text[i][4]
        LastNameTH = text[i][5]
        IDType = text[i][6]
        PassportCountry = text[i][7]
        IDNo = text[i][8]
        IDExpiryDate = text[i][9]
        BirthDate = text[i][10]
        Email = text[i][11]
        Phone = text[i][12]
        Fax = text[i][13]
        Position = text[i][14]
        AuthorizationFlag = text[i][15]
        Relationship = text[i][16]
        RelationshipOther = text[i][17]
        IdentificationDocumentAddressNo = text[i][18]
        IdentificationDocumentMoo = text[i][19]
        IdentificationDocumentPlace = text[i][20]
        IdentificationDocumentRoomNo = text[i][21]
        IdentificationDocumentFloor = text[i][22]
        IdentificationDocumentSoi = text[i][23]
        IdentificationDocumentRoad = text[i][24]
        IdentificationDocumentTambon = text[i][25]
        IdentificationDocumentAmphur = text[i][26]
        IdentificationDocumentProvince = text[i][27]
        IdentificationDocumentPostalCode = text[i][28]
        IdentificationDocumentCountry = text[i][29]
        CurrentAddressNo = text[i][30]
        CurrentMoo = text[i][31]
        CurrentPlace = text[i][32]
        CurrentRoomNo = text[i][33]
        CurrentFloor = text[i][34]
        CurrentSoi = text[i][35]
        CurrentRoad = text[i][36]
        CurrentTambon = text[i][37]
        CurrentAmphur = text[i][38]
        CurrentProvince = text[i][39]
        CurrentPostalCode = text[i][40]
        CurrentCountry = text[i][41]
        CEOFlag = text[i][42]
        PoliticianFlag = text[i][43]
        PoliticianPosition = text[i][44]
        Nationality = text[i][45]
        RegisterCountry = text[i][46]
        AsOfDate = dateFile(file_customer_detail)

        database.insert(
            """
                INSERT INTO FCN_CustomerProfileDetail
                (
                    NewUnitholderIDReferenceNo, UnitholderIDReferenceNo, Type, Sequence, ParentReferenceID, FirstNameTH, 
                    LastNameTH, IDType, PassportCountry, IDNo, IDExpiryDate, BirthDate, Nationality, Email, Phone, Fax, Position, 
                    AuthorizationFlag, Relationship, RelationshipOther,  IdentificationDocumentAddressNo, 
                    IdentificationDocumentMoo, IdentificationDocumentPlace, IdentificationDocumentRoomNo, IdentificationDocumentFloor, 
                    IdentificationDocumentSoi, IdentificationDocumentRoad, IdentificationDocumentTambon, IdentificationDocumentAmphur, 
                    IdentificationDocumentProvince, IdentificationDocumentPostalCode, IdentificationDocumentCountry, CurrentAddressNo, 
                    CurrentMoo, CurrentPlace, CurrentRoomNo, CurrentFloor, CurrentSoi, CurrentRoad, CurrentTambon, CurrentAmphur, 
                    CurrentProvince, CurrentPostalCode, CurrentCountry, CEOFlag, PoliticianFlag, PoliticianPosition, 
                    RegisterCountry, AsOfDate
                )

                VALUES
                (
                    '""" + NewUnitholderIDReferenceNo + """', '""" + UnitholderID + """', '""" + Type + """', 
                    '""" + Sequence + """', '""" + ParentReferenceID + """', '""" + FirstNameTH + """', 
                    '""" + LastNameTH + """', '""" + IDType + """', '""" + PassportCountry + """', '""" + IDNo + """', 
                    '""" + IDExpiryDate + """', '""" + BirthDate + """', '""" + Nationality + """', '""" + Email + """', 
                    '""" + Phone + """', '""" + Fax + """', '""" + Position + """', '""" + AuthorizationFlag + """', 
                    '""" + Relationship + """', '""" + RelationshipOther + """', 
                    '""" + IdentificationDocumentAddressNo + """', '""" + IdentificationDocumentMoo + """', 
                    '""" + IdentificationDocumentPlace + """', '""" + IdentificationDocumentRoomNo + """', 
                    '""" + IdentificationDocumentFloor + """', '""" + IdentificationDocumentSoi + """', 
                    '""" + IdentificationDocumentRoad + """', '""" + IdentificationDocumentTambon + """', 
                    '""" + IdentificationDocumentAmphur + """', '""" + IdentificationDocumentProvince + """', 
                    '""" + IdentificationDocumentPostalCode + """', '""" + IdentificationDocumentCountry + """', 
                    '""" + CurrentAddressNo + """', '""" + CurrentMoo + """', '""" + CurrentPlace + """', '""" + CurrentRoomNo + """', 
                    '""" + CurrentFloor + """', '""" + CurrentSoi + """', '""" + CurrentRoad + """', '""" + CurrentTambon + """', 
                    '""" + CurrentAmphur + """', '""" + CurrentProvince + """', '""" + CurrentPostalCode + """', 
                    '""" + CurrentCountry + """', '""" + CEOFlag + """', '""" + PoliticianFlag + """', 
                    '""" + PoliticianPosition + """', '""" + RegisterCountry + """', '""" + AsOfDate + """'
                )
            """
        )

        print('CustomerProfileDetail - Upload UHID: {0}, Name: {1}'.format(UnitholderID, FirstNameTH))


customer_profile_detail()