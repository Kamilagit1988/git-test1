import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEX NOT NULL, 
age INTEGER,
balance INTEGER 
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",  (f"User{i+1}", f"example{i+1}@gmail.com", f"{(i+1)*10}", "1000"))

cursor.execute("UPDATE Users SET balance = ? WHERE id%2 <> ?", (500, 0))

cursor.execute("DELETE FROM Users WHERE (id+2)%3 = ?", (0,))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс {user[3]}")

#cursor.execute("SELECT * FROM Users")


#cursor.execute("SELECT username, age FROM Users WHERE age >?",(5,))

#cursor.execute(" SELECT age, AVG(age) FROM Users GROUP BY AGE")
#users = cursor.fetchall()

#    print(user)
connection.commit()
connection.close()