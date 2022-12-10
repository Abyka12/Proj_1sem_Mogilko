# Вариант 29
# Выполнить сортировку словаря d = {'a': 5, 'b': 30, 'c': 3}


d = {'a': 5, 'b': 30, 'c': 3}
items = d.items
print(f"Дан словарь {d}, его нужно отсортировать")
a = input("Выберите тип сортировки: \n"
          "1 - ключи \n"
          "2 - значения\n"
          "Введите знаечние: ")

if a == '1':
    sorted_items = sorted(items(), key=lambda x: x[0])
    print(dict(sorted_items))

elif a == '2':
    sorted_items = sorted(items(), key=lambda x: x[1])
    print(dict(sorted_items))

else:
    print("Введено неверное значение")
