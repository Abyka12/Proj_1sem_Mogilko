# Вариант 29
# В матрице элементы последнего столбца заменить на -1.


from random import randint

n = int(input("Введите размер марицы: "))

matrix = [[randint(-10, 10) for j in range(n)] for i in range(n)]

print("Исходная матрица:")
for i in matrix:
    print(i, sep='\t')

for i in matrix:
    i[n-1] = -1

print("\nГотовая матрица:")
for i in matrix:
    print(i, sep='\t')
