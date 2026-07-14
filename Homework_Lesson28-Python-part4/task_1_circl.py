#!/usr/bin/env python3

class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def square(self):
        print(f"Площадь окружности: {3.14 * self.radius**2} м^2")

    def len_circle(self):
        print(f"Длина окружности: {2 * 3.14 * self.radius} м")
    
    def circle_color(self):
        print(f"Цвет круга: {self.color}")


calc = Circle(2, "Black")
calc_1 = Circle(4, "Pink")
calc_2 = Circle(8, "Red")

calc.square()
calc.len_circle()
calc.circle_color()

calc_1.square()
calc_1.len_circle()
calc_1.circle_color()

calc_2.square()
calc_2.len_circle()
calc_2.circle_color()
