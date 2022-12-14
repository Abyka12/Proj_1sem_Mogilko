# Вариант 29

# Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено
# максимально возможное количество квадратов со стороной C (без наложений).
# Найти количество квадратов, размещенных на прямоугольнике. Операции
# умножения и деления не использовать.


while True:  # Цикл проверки типа переменной
    try:
        a = int(input("Введите A: "))
        break
    except:
        print("Попробуйте еще раз!")

while True:  # Цикл проверки типа переменной
    try:
        b = int(input("Введите B: "))
        break
    except:
        print("Попробуйте еще раз!")

while True:  # Цикл проверки типа переменной
    try:
        c = int(input("Введите C: "))
        break
    except:
        print("Попробуйте еще раз!")

i = 0  # Счетчик квадратов
a1 = a  # Временная переменная для использования в цикле

if (a < c) or (b < c):  # Проверка, можно ли поместить хотя бы один квадрат
    print("Невозможно поместить ни одного квадрата")

else:
    while b >= c:
        while a1 >= c:
            a1 -= c  # Отсечение стороны квадрата от длины прямоугольника
            i += 1  # Увеличение счетчика
        a1 = a  # Присвоение временной переменной значения А в конце цикла
        b = b - c  # Отсечение стороны квадрата от ширины прямоугольника

print("Количество квадратов:", i)  # Вывод итогового значения
