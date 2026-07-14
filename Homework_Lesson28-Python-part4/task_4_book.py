#!/usr/bin/env python3

class Book:
    def __init__(self, name, author, year):
        self.__name = name
        self.__author = author
        self.__year = year

    def get_name(self):
        return self.__name
    
    def get_author(self):
        return self.__author
    
    def get_year(self):
        return self.__year
    
    def set_name(self, new_name):
        if new_name:
            self.__name = new_name
            print(f"Название изменено: {self.__name}")

    def set_author(self, new_author):
        if new_author:
            self.__author = new_author
            print(f"Автор изменен: {self.__author}")

    def set_year(self, new_year):
        if new_year:
            self.__year = new_year
            print(f"Год изменен: {self.__year}")

book_1 = Book("Три товарища", "Эрих Мария Ремарк", "1956")
book_2 = Book("Трое в лодке", "Джером Клапка", "1976")

print(f"Название книги: {book_1.get_name()}")
print(f"Автор: {book_1.get_author()}")
print(f"Год издания: {book_1.get_year()}")

book_1.set_name("Два товарища")
book_1.set_author("Андрей Пупкин")
book_1.set_year(1967)

print(f"Название книги: {book_2.get_name()}")
print(f"Автор: {book_2.get_author()}")
print(f"Год издания: {book_2.get_year()}")

book_2.set_name("Дети капитана Гранта")
book_2.set_author("Жюль Верн")
book_2.set_year(1875)
