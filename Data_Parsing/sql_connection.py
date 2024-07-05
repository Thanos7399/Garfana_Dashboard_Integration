import mysql.connector
from mysql.connector import Error

def check_mysql_connection(host, user, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='einfochips',
            password='Einfochips@123'
        )

        if connection.is_connected():
            print("Connected to MySQL server")
            connection.close()
        else:
            print("Failed to connect to MySQL server")

    except Error as e:
        print("Error while connecting to MySQL", e)

# Replace with your actual details
check_mysql_connection('10.126.31.6', 'sahil', 'einfochips@123')
