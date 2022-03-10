import pyodbc


class SQL:

    def __init__(self, db_name, ser_name, user, password):
        self.db_name = db_name
        self.ser_name = ser_name
        self.user = user
        self.password = password

    def connect_database(self):
        conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=' + self.ser_name + ';'
            'Database=' + self.db_name + ';'
            'uid=' + self.user + ';'
            'pwd=' + self.password + ';'
        )
        cursor = conn.cursor()
        return cursor

    def query(self, query):
        cursor = self.connect_database()
        cursor.execute(
            """
            """ + query + """
            """
        )
        return cursor

    def commit(self, commit):
        cursor = self.connect_database()
        cursor.execute(
            """
            """ + commit + """
            """
        )
        cursor.commit()
        return cursor


# -- Setting connect database
database = SQL('Fundconnext_PRD', '192.168.100.5', 'sa', 'EnSEC$999')
