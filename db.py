import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cloven_faction"
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Insert data into the table
def insert_data(product_code, product_name, brand, price, quantity):
    query = "INSERT INTO cloven(product_code, product_name, brand, price, quantity) VALUES (%s, %s, %s, %s, %s)"
    values = (product_code, product_name, brand, price, quantity)
    cursor.execute(query, values)
    cnx.commit()
    print("Data inserted successfully!")

# Remove data from the table
def remove_data(product_code):
    query = "DELETE FROM cloven_faction WHERE product_code = %s"
    values = (product_code,)
    cursor.execute(query, values)
    cnx.commit()
    print("Data removed successfully!")

# Fetch all data from the table
def fetch_data():
    query = "SELECT * FROM cloven_faction"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Search data in the table
def search_data(product_name):
    query = "SELECT * FROM cloven_faction WHERE product_name = %s"
    values = (product_name,)
    cursor.execute(query, values)
    result = cursor.fetchall()
    for row in result:
        print(row)

# Example usage
insert_data(1, 'Shirt', 'Cloven Faction', 29.99, 50)
remove_data(1)
fetch_data()
search_data('Shirt')

# Close the cursor and connection
cursor.close()
cnx.close()