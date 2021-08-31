import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    print("Connection successful!!")
    conn.execute("CREATE TABLE user (name VARCHAR(100))")
    conn.close()

def show_all():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = "SELECT * FROM user"
    users = cursor.execute(query)
    for i in users:
        print(i)