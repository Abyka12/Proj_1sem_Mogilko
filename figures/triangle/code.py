__all__ = ['triangle_perimeter', 'triangle_area']

d_a = 7
d_b = 2
d_c = 8


def triangle_perimeter(a=d_a, b=d_b, c=d_c):
    print("Периметр треугольника = ", a+b+c)


def triangle_area(a=d_a, b=d_b, c=d_c):
    p = (a+b+c)/2
    area = (p*(p-a)*(p-b)*(p-c))**(1/2)
    print("Площадь треугольника = ", area)
