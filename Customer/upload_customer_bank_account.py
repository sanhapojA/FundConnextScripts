from module_read_text import read_text
from datetime import datetime, date
from module_connect_database import SQL
from module_customer import *

# date = '20211229'

date = datetime.today()
date = date.strftime('%Y%m%d')


# read text customer.txt
file_customer_bank = r'P:/FundConnext/FundConnext-PRD/Download Files/' + date + '/' + date + '_XSpringAM_NEWACCOUNT/' + date + '_XSpringAM_CUSTOMER_BANK_ACCOUNT.txt'
text = read_text(1, file_customer_bank)

# connect database
database = SQL('Fundconnext_PRD', '192.168.100.5', 'sa', 'EnSEC$999')

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


def customer_bank_account():
    for i in range(len(text)):
        NewUnitholderIDReferenceNo = text[i][0]
        UnitholderID = unitholder_id(NewUnitholderIDReferenceNo)
        TransactionCode = text[i][1]
        BankCode = text[i][2]
        BankAccount = text[i][3]
        BankaccountName = text[i][4]
        Defaultaccount = text[i][5]
        BankBranchCode = text[i][6]

        AsOfDate = dateFile(file_customer_bank)

        database.insert(
            """
                INSERT INTO FCN_BankAccount
                (
                    NewUnitholderIDReferenceNo, UnitholderIDReferenceNo, TransactionCode, BankCode, BankAccount, BankAccountName, 
                    DefaultAccount, BankBranchCode, AsOfDate
                )

                VALUES
                (
                    '""" + NewUnitholderIDReferenceNo + """', '""" + UnitholderID + """', '""" + TransactionCode + """', 
                    '""" + BankCode + """', '""" + BankAccount + """', '""" + BankaccountName + """', '""" + Defaultaccount + """', 
                    '""" + BankBranchCode + """', '""" + AsOfDate + """'

                )
            """
        )

        print(
            'Customer Bank Account - Upload UHID: {0}, Transaction Code: {1}'.format(UnitholderID, TransactionCode))


customer_bank_account()  