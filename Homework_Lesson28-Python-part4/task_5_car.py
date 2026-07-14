#!/usr/bin/env python3

class Car:
    def __init__(self, brand, model, color, year):
        self.__brand = brand
        self.__model = model
        self.__color = color
        self.__year = year
    
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
    
    def get_year(self):
        return self.__year
    
    def set_brand(self, new_brand):
        if new_brand:
            self.__brand = new_brand
            print(f"Марка автомобиля изменена: {self.__brand}")

    def set_model(self, new_model):
        if new_model:
            self.__model = new_model
            print(f"Модель автомобиля изменена: {self.__model}")
    
    def set_color(self, new_color):
        if new_color:
            self.__color = new_color
            print(f"Цвет автомобиля изменен: {self.__color}")
    
    def set_year(self, new_year):
        if new_year:
            self.__year = self.__year
            print(f"Год выпуска изменен: {self.__year}")

car_1 = Car("Toyota", "Camry", "Черный", 1989)
car_2 = Car("BMW", "X5", "Белый", 1976)

print(f"Марка автомобиля: {car_1.get_brand()}")
print(f"Модель автомобиля: {car_1.get_model()}")
print(f"Цвет автомобиля: {car_1.get_color()}")
print(f"Год выпуска: {car_1.get_year()}")

car_1.set_brand("Mersedes")
car_1.set_model("Benz")
car_1.set_color("Красный")
car_1.set_year(1990)

print(f"Марка автомобиля: {car_2.get_brand()}")
print(f"Модель автомобиля: {car_2.get_model()}")
print(f"Цвет автомобиля: {car_2.get_color()}")
print(f"Год выпуска: {car_2.get_year()}")

car_2.set_brand("Range Rover")
car_2.set_model("Sport")
car_2.set_color("Зеленый")
car_2.set_year(2021)
