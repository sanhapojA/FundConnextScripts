import pyodbc


class SQL:

    def __init__(self, db_name, ser_name, user, password):
        self.db_name = db_name
        self.ser_name = ser_name
        self.user = user
        self.password = password

    def connect_db(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=' + self.ser_name + ';'
                              'Database=' + self.db_name + ';'
                              'uid=' + self.user + ';'
                              'pwd=' + self.password + ';'
                              'Trusted_Connection=no;')

        cursor = conn.cursor()
        return cursor

    def query(self, query):
        cursor = self.connect_db()
        cursor.execute(""" 
                            """ + query + """ 
                        """
                       )
        return cursor

    # insert, update, delete
    def statements(self, crud):
        cursor = self.connect_db()
        cursor.execute(""" 
                            """ + crud + """ 
                        """
                       )
        cursor.commit()
        return cursor

    def insert(self, insert):
        return self.statements(insert)

    def update(self, update):
        return self.statements(update)

    def delete(self, delete):
        return self.statements(delete)
