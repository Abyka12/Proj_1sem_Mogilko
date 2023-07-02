# Вариант 29
# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Элементы первого и второго файлов:
# Количество элементов первого и второго файлов:
# Количество элементов, общих для двух файлов:
# Количество четных элементов первого файла:
# Количество нечетных элементов второго файла:


from random import randint

f1 = [randint(-5, 5) for i in range(10)]
f2 = [randint(-5, 5) for i in range(10)]

f1_even = len([i for i in f1 if i % 2 == 0 and i != 0])
f2_even = len([i for i in f2 if i % 2 == 0 and i != 0])


def create_file1():
    with open('file1.txt', 'w+') as f:
        for item in f1:
            f.write("%s\n" % item)
    f.close()


def create_file2():
    with open('file2.txt', 'w+') as f:
        for item in f2:
            f.write("%s\n" % item)
    f.close()


create_file1()
create_file2()
common_elements = len(set(f1) & set(f2))

with open('file3.txt', 'w+') as f:
    f.write("Элементы первого файла: ")
    for i in f1:
        f.write(f"{i} ")
    f.write('\n')
    f.write("Элементы второго файла: ")
    for i in f2:
        f.write(f"{i} ")
    f.write('\n')
    f.write(f"Количество элементов первого файла: {len(f1)}\n")
    f.write(f"Количество элементов второго файла: {len(f2)}\n")
    f.write(f"Количество общих элементов: {common_elements}\n")
    f.write(f"Количество четных в первом файле: {f1_even}\n")
    f.write(f"Количество четных во втором файле: {f2_even}\n")
