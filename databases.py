import mysql.connector as sql


mydbs = sql.connect(
    host="localhost",
    user="root",
    password="Kushi@2004",
    database="Bank"
    )

cursor = mydbs.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result   

def createcustomertable():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Customers
            (username VARCHAR(20),
            password VARCHAR(20),
            name VARCHAR(20),
            age INTEGER,
            city VARCHAR(20),
            account_number INTEGER,
            balance INTEGER,
            status BOOLEAN)

''') 

mydbs.commit()

if __name__ == "__main__":
    createcustomertable()