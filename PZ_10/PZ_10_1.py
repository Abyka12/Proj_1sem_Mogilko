

Magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
DomKnigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BukMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galereya = {"Чехов", "Тютчев", "Пушкин"}

shops = {"ДомКниги": {"Толстой", "Грибоедов", "Чехов", "Пушкин"},
         "Магистр": {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}}

grib = []
if "Грибоедов" not in Magistr:
    grib.append("Магистр")
if "Грибоедов" not in DomKnigi:
    grib.append("ДомКниги")
if "Грибоедов" not in BukMarket:
    grib.append("БукМаркет")
if "Грибоедов" not in Galereya:
    grib.append("Галерея")

print("Книг Грибоедова нельзя купить в магазинах:", end = ' ')
for i in grib:
    print(i, end=' ')
print()

mayak = []
if "Маяковский" not in Magistr:
    mayak.append("Магистр")
if "Маяковский" not in DomKnigi:
    mayak.append("ДомКниги")
if "Маяковский" not in BukMarket:
    mayak.append("БукМаркет")
if "Маяковский" not in Galereya:
    mayak.append("Галерея")

print("Книг Маяковского нельзя купить в магазинах:", end=' ')
for i in mayak:
    print(i, end=' ')



