# Вариант 29

# Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# ее помощью для данных переменных A, B, C, D последовательно поменять
# содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C, D.


while True:  # Цикл проверки типа переменной А
    try:
        a = int(input("Введите A: "))
        break
    except:
        print("Попробуйте еще раз!")

while True:  # Цикл проверки типа переменной B
    try:
        b = int(input("Введите B: "))
        break
    except:
        print("Попробуйте еще раз!")

while True:  # Цикл проверки типа переменной C
    try:
        c = int(input("Введите C: "))
        break
    except:
        print("Попробуйте еще раз!")

while True:  # Цикл проверки типа переменной D
    try:
        d = int(input("Введите D: "))
        break
    except:
        print("Попробуйте еще раз!")


def swap(x, y):  # Описание функции swap с аргументами Х и У
    t = x  # Введение временной переменной Т, присвоение ей значения Х
    x = y  # Присвоение Х значения У
    y = t  # Присвоение У значения Т, которое является бывшим значением Х
    return x, y  # Возврат результата работы функции в кортеже


a, b = swap(a, b)  # \
c, d = swap(c, d)  # Поочередная замена значений у нужных пар чисел с помощью функции
b, c = swap(b, c)  # /

print(a, b, c, d)  # Вывод результата
