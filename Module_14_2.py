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

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE username = ?", ("User6",))
# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances/total_users)

connection.commit()
connection.close()