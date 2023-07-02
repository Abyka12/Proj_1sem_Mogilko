import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
filling = """INSERT INTO Туры ("название", "страна", "город", "дата_начала", "дата_окончания", "цена") 
                VALUES ('Париж', 'Франция', 'Париж', '2019-09-15', '2019-10-15', 500.00);"""

cursor.execute(filling)
a = """SELECT * FROM Туры"""
cursor.execute(a)
records = cursor.fetchall()


print(records)
