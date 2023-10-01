import mysql.connector as connector

mydb = connector.connect(host='localhost',
            user = 'root',
            password='',
            database = 'cloven_faction',
        )

print(mydb)


# quary = 'create table if not exists cloven_faction(product_code INT PRIMARY KEY, product_name VARCHAR(255) brand VARCHAR(255), price DECIMAL(10,2), quantity INT'


# cursr =  mydb.cursor()
# cursr.execute(quary)

# print(cursr)

def insert_data(  ProductCode, productName, brand, price, quantity):
    quary = f"INSERT INTO cloven_faction(product_code, product_name, brand, price, quantity)VALUES ({ProductCode}, '{productName}', '{brand}',{price}, {quantity})"
    cursr =  mydb.cursor()
    cursr.execute(quary)
    mydb.commit()

def fech_data():
    quary = 'select * from cloven_faction'
    cursr =  mydb.cursor()
    cursr.execute(quary)
    return cursr

def remove_data(productCode):
    query = f"DELETE FROM cloven_faction WHERE product_code = {productCode}"
    cursr =  mydb.cursor()
    cursr.execute(query)
    mydb.commit()
    
def search_data(product_code):
    query = f"SELECT * FROM cloven_faction WHERE product_code = '{product_code}'"
    cursr =  mydb.cursor()
    cursr.execute(query)
    result = cursr.fetchall()
    return result