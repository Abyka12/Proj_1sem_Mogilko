# Вариант 29

# Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
# методы для определения дня недели, проверки на високосный год и определения
# количества дней в месяце.
class Calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def weekday(self):
        pass

    def is_leap(self):
        if self.year % 4 == 0:
            return True
        else:
            return False

    def days(self):
        if self.is_leap() and self.month == 2:
            return 29
        elif self.month == 2:
            return 28
        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30


# Создайте базовый класс "Животное" со свойствами "вид", "количество лап", "цвет
# шерсти". От этого класса унаследуйте класс "Собака" и добавьте в него свойства
# "кличка" и "порода".
class Animal:
    def __init__(self, kind, legs, color):
        self.kind = kind
        self.legs = legs
        self.color = color


class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__("Собака", 4, color)
        self.name = name
        self.breed = breed
