# Задание 1: Базовый класс и методы
# 1. Определите класс Book, который имеет три атрибута: title (название),
# author (автор), и year (год издания).
# 2. Добавьте метод get_info(), который возвращает информацию о книге в
# формате: "Название книги: [title], Автор: [author], Год издания: [year]".


class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"


# Пример использования
book_1 = Book("1984", "Джордж Оруэлл", 1949)
print(book_1.get_info())
