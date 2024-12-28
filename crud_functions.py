import sqlite3

connection = sqlite3.connect("base.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEX, 
price INTEGER NOT NULL
);
''')

def initiate_db(id, title, description, price):
    check_user = cursor.execute( "SELECT * FROM Products WHERE id=?", (id,))

    if check_user.fetchone() is None:
        cursor.execute(f'''
    INSERT INTO Products VALUES ('{id}', '{title}', '{description}', {price} )    
    ''')

initiate_db(1, 'Продукт 1', 'описание 1', 100)
initiate_db(2, 'Продукт 2', 'описание 2', 200)
initiate_db(3, 'Продукт 3', 'описание 3', 300)
initiate_db(4, 'Продукт 4', 'описание 4', 400)


def get_all_products():
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Products WHERE id > ?', (0,))
    return cursor.fetchall()



connection.commit()
connection.close()