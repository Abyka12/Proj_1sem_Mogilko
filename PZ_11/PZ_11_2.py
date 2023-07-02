# Вариант 29
# Из предложенного текстового файла (text18-29.txt) вывести на экран его содержимое,
# количество символов в тексте. Сформировать новый файл, в который поместить текст в
# стихотворной форме предварительно поставив последнюю строку между второй и третьей.

with open("text18-29.txt", 'r+', encoding='utf-16') as f:
    file_lines = f.readlines()
    f.close()

with open("text18-29.txt", 'r+', encoding='utf-16') as f:
    file_content = f.read()
    f.close()

file_lines[-1] = file_lines[-1] + '\n'
file_lines[2], file_lines[-1] = file_lines[-1], file_lines[2]
print(f"Количество символов в тексте: {len(file_content)}")

with open("text18-29_2.txt", 'w+') as f:
    for i in file_lines:
        f.write(i)
    f.close()
