
Magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
DomKnigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BukMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galereya = {"Чехов", "Тютчев", "Пушкин"}  # Заданные значения

grib = []  # Cписок, в котором хранятся названия магазинов
if "Грибоедов" not in Magistr:  # Проверка отсутствия книги в магазине
    grib.append("Магистр")
if "Грибоедов" not in DomKnigi:  # Проверка отсутствия книги в магазине
    grib.append("ДомКниги")
if "Грибоедов" not in BukMarket:  # Проверка отсутствия книги в магазине
    grib.append("БукМаркет")
if "Грибоедов" not in Galereya:  # Проверка отсутствия книги в магазине
    grib.append("Галерея")

print("Книг Грибоедова нельзя купить в магазинах:", end = ' ')
for i in grib:
    print(i, end=' ')  # Вывод значений Списка
print() # Перенос на новую строку

mayak = []  # Список, в котором хранятся названия магазинов
if "Маяковский" not in Magistr:  # Проверка отсутствия книги в магазине
    mayak.append("Магистр")
if "Маяковский" not in DomKnigi:  # Проверка отсутствия книги в магазине
    mayak.append("ДомКниги")
if "Маяковский" not in BukMarket:  # Проверка отсутствия книги в магазине
    mayak.append("БукМаркет")
if "Маяковский" not in Galereya:  # Проверка отсутствия книги в магазине
    mayak.append("Галерея")

print("Книг Маяковского нельзя купить в магазинах:", end=' ')
for i in mayak:
    print(i, end=' ')  # Вывод значений Списка
