# Вариант 29
#

c = input('Введите С: ')
s = input('Введите S: ')
s0 = input('Введите S0: ')
counter = 0
s1 = ''
# is_c = 0

for i in s:
    s1 += i
    if i == c:
        s1 += s0

print(s1)
