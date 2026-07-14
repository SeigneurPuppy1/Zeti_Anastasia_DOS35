#!/usr/bin/env python3

class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def average_score(self):
        sr = round(sum(self.score) / len(self.score), 2)
        print(f"Студент: {self.name}\n Возраст: {self.age}\n Средний балл: {sr}")

        if 2.5 < sr < 4:
            print("Статус: Троечник")
        elif 5 > sr >= 4:
            print("Статус: Хорошист")
        elif sr == 5:
            print("Статус: Отличник")

student_1 = Student("Смирнов Алексей", 21, [4, 5, 4, 3])
student_2 = Student("Петров Максим", 22, [4, 3, 4, 2])
student_3 = Student("Калинин Сергей", 24, [4, 5, 4, 5])

student_1.average_score()
student_2.average_score()
student_3.average_score()
