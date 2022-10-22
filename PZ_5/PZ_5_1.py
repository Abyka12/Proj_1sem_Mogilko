# Вариант 29

# Составить функцию, которая напечатает сорок любых символов.

import random

letters = "qwertyuiopasdfghjklzxcvbnm1234567890.,йцукенгшщзхъфывапролджэячсмитьбюё!№;%:?*()_+-="


def print40():
    a = 0
    while a < 40:
        print(random.choice(letters), end=' ')
        a += 1


print40()
