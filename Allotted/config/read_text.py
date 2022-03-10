from datetime import datetime

class FundFiles:

    def __init__(self, fileName, startLine=0):
        self.start_line = startLine
        self.file_name = fileName

    def read_text(self):
        text = []
        with open(self.file_name, 'r', encoding='UTF-8') as fn:
            read_files_name = fn.readlines()
            for i in range(self.start_line, len(read_files_name)):
                read_col = read_files_name[i].split('|')
                text.append(read_col)
        return text
    
    def file_date(self):
        file_date = self.read_text()
        return file_date
    
    def count_line(self):
        with open(self.file_name, 'r', encoding='UTF-8') as fn:
            readFilesName = fn.readlines()
        return str(int(len(readFilesName)) - 1)


# dateToday = '20210916'
dateToday = datetime.today()
dateToday = dateToday.strftime('%Y%m%d')


#-- Setting read text file "NEWACCOUNT".
try:
    path_file_new_customer = r'P:/FundConnext/FundConnext-PRD/Download Files/' + dateToday + '/' + dateToday + '_XSPRINGAM_NEWACCOUNT/' + dateToday + '_XSpringAM_CUSTOMER.txt'
    file_new_customer = FundFiles(path_file_new_customer, startLine=1).read_text()
except:
    pass


#-- Setting read text file "PAIDTRANSACTIONS".
try:
    path_file_paidtransaction = r'P:/FundConnext/FundConnext-PRD/Download Files/' + dateToday + '/' + dateToday + '_XSPRINGAM_PAIDTRANSACTIONS/' + dateToday + '_XSpringAM_PAIDTRANSACTIONS.txt'
    file_paidtransaction = FundFiles(path_file_paidtransaction, startLine=1).read_text()
except:
    pass


#-- Make folder file "ALLOTTEDTRANSACTIONS".
try:
    path_folder_allotted = r'P:/FundConnext/FundConnext-PRD/Upload Files/' + dateToday + '/Allotted/'
except:
    pass


#-- Setting save file "ALLOTTEDTRANSACTIONS".
try:
    path_file_allotted = r'P:/FundConnext/FundConnext-PRD/Upload Files/' + dateToday + '/Allotted/' + dateToday + '_XSpringAM_ALLOTTEDTRANSACTIONS.txt'
    file_allotted = FundFiles(path_file_allotted, startLine=1).read_text()
except:
    pass


#-- file date.
try:
    file_date = FundFiles(path_file_new_customer, startLine=0).file_date()
    file_date = file_date[0][0]
except:
    pass


#-- total lines transaction.
try:
    total_line_transaction = FundFiles(path_file_paidtransaction, startLine=0).count_line()
except:
    pass