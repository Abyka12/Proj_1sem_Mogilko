__all__ = ['circle_perimeter', 'circle_area']

default_radius = 5


def circle_perimeter(rad=default_radius):
    perimeter = 2 * rad * 3.14
    print("Радиус = ", rad)
    print("Длина окружности:", perimeter)


def circle_area(rad=default_radius):
    area = rad * rad * 3.14
    print("Радиус = ", rad)
    print("Площадь окружности:", area)
