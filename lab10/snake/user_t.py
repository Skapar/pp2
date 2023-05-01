import psycopg2
from config import *

#connecting to our database
conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

#creating table for user if not exists
conn.autocommit = True
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                (id SERIAL PRIMARY KEY, 
                username VARCHAR(255) UNIQUE)''')

cursor.close()
conn.close()