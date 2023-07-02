# Вариант 1
#

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('test.db')

# Создание таблиц
create_table_tour = """CREATE TABLE IF NOT EXISTS Туры (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    название TEXT,
    страна TEXT,
    город TEXT,
    дата_начала TEXT,
    дата_окончания TEXT,
    цена REAL)"""

create_table_tourist = """CREATE TABLE IF NOT EXISTS Туристы (
    id INTEGER PRIMARY KEY,
    имя TEXT,
    фамилия TEXT,
    пол TEXT,
    дата_рождения TEXT,
    номер_телефона TEXT,
    электронная_почта TEXT)"""

create_table_booking = """CREATE TABLE IF NOT EXISTS Бронирования (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_турист INTEGER,
    id_тур INTEGER,
    дата_бронирование TEXT,
    кол_во_туристы INTEGER,
    FOREIGN KEY(id_турист) REFERENCES id(Туристы),
    FOREIGN KEY(id_тур) REFERENCES id(Туры))"""

conn.execute(create_table_tour)
conn.execute(create_table_tourist)
conn.execute(create_table_booking)


# Заполнение таблиц данными
add_data_tour = """INSERT INTO Туры VALUES (1, 'Париж', 'Франция', 'Париж', '2019-09-15', '2019-10-15', 500.00);"""
add_data_tourist = """INSERT INTO Туристы VALUES (1, 'Иван', 'Иванов', 'М', '1990-01-01', '+7 (123) 456-78-90', 'ivanov@mail.com')"""
add_data_booking = """INSERT INTO Бронирования VALUES (1, 1, 1, '2018-08-15', 3)"""

for add_data in [add_data_tour, add_data_tourist, add_data_booking]:
    conn.execute(add_data)

conn.commit()  # Сохраняем изменения в базе данных
