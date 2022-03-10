from module_connect_database import SQL
from module_read_text import read_text

# connect database
databaseZmico = SQL('Zmico_Asset', '192.168.100.5', 'sa', 'EnSEC$999')


def countZero(number, round):
    zero = ''
    for _ in range(number, round):
        zero += '0'
    return zero


def dateFile(filename):
    dateFiles = read_text(0, filename)
    dateFile = dateFiles[0][0]
    return dateFile


class UHID:

    def __init__(self, idNo, date):
        self.idNo = idNo
        self.date = date

    def unitholder_id(self):
        find_uhid = databaseZmico.query(
            """
                SELECT STRHOLDERID, STRREFNO
                FROM M_UNITHOLDER
                WHERE STRREFNO = '""" + self.idNo + """' AND [DTETRANSDATE] = '"""+ self.date +"""'
            """
        )

        try:
            for row in find_uhid:
                uhid = row[0]
            return uhid

        except:
            return None