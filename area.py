import math


def calculate_circle_area(radius):
    return round(radius**2 * math.pi, 2)


def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    return False


def calculate_triangle_area(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError(
            "Стороны треугольника должны быть положительными числами")
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        raise ValueError(
            "Треугольник с заданными сторонами невозможно построить")
    if is_right_triangle(side1, side2, side3):
        print("Этот треугольник является прямоугольным")

    p = (side1 + side2 + side3) / 2
    area = math.sqrt(p * (p - side1)*(p - side2)*(p - side3))
    return round(area, 2)


def figure_type(data: list):
    number = len(data)
    if number == 1:
        return f"Площадь круга {calculate_circle_area(data[0])}"
    if number == 2:
        raise ValueError("Такой фигуры не существует")
    if number == 3:
        return f"Площадь треугольника {calculate_triangle_area(data[0], data[1], data[2])}"
