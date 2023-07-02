# Вариант 29
# Составить генератор (yield), который преобразует все буквенные символы в
# строчные.


def lower_case(s):
    for char in s:
        yield char.lower()


st = ""
for i in lower_case(input("Введите предложение:\n")):
    st = st + i

print(st)
