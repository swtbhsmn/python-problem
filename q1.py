# Q1.   Create a table with a large number of records (you can find it with a google search 
#       or use this link - https://github.com/datacharmer/test_db). Use MySQL Database.One can
#       setup MySQL on localhost. Write some basic queries using python. Suppose you want to 
#       process/fetch a large number of records using python while keeping your memory usage low.
#       Think of approaches on how to accomplish this and Implement.
#       Hint: Use Generator


import pymysql

class MySQLConnection:
    def __init__(self, hostname: str, user: str, password: str, database: str, port: int=3306):
         self.hostname = hostname
         self.user= user
         self.password = password
         self.database = database
         self.port = port
         self.connection = None

    def __repr__(self):
        return f'{self.user}@{self.hostname}'
         
    def __enter__(self):
        self.connection = pymysql.connect(host=self.hostname, user=self.user, password = self.password, db=self.database)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()

def cursor_iter(cursor):
    while True:
        rows = cursor.fetchall()
        if not rows: break
        for row in rows:
            yield row

def main():
    with MySQLConnection(hostname="localhost",user="admin",password="Swetabh1@",database="employees",port=3306) as db: # utilize db Create cursor
        pointer = db.connection.cursor()
        query = """SELECT * FROM employees.employees"""
        pointer.execute(query)
        gen = cursor_iter(pointer)
        for _ in range(10):
            print(next(gen))
        

if __name__ == '__main__':
     main()
