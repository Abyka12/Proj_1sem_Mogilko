# Вариант 29
# В матрице элементы третьей строки заменить элементами из одномерного
# динамического массива соответствующей размерности.


from random import randint

n = int(input("Введите размер марицы: "))

matrix = [[randint(-10, 10) for i in range(n)] for j in range(n)]

print("Исходная матрица:")
for i in matrix:
    print(i, sep='\t')

array = [randint(-10, 10) for i in range(n)]

print(f"Исходный массив: {array}")

matrix[2] = array

print("\nГотовая матрица:")
for i in matrix:
    print(i, sep='\t')
