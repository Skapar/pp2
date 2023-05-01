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
cursor.execute('''CREATE TABLE IF NOT EXISTS user_score 
               (id SERIAL PRIMARY KEY, 
               user_id INTEGER REFERENCES users(id), 
               score INTEGER)''')

cursor.close()
conn.close()