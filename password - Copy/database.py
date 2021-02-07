import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'PASSWORDS'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
