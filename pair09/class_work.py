# # book_dict = {
# #     "title": "Кобзар",
# #     "author": "Тарас Шевченко",
# #     "copies": 15
# # }
# # print(book_dict["title"])


# class Book:
#     def __init__(self, title):
#         self.title = title

#     def __str__(self):
#         return self.title

# book1 = Book("Кобзар")
# book2 = Book("Лісова пісня")

# print(book1, book2) 
# # Тепер виведе: Кобзар Лісова пісня


# class Book:
#     def __init__(self, title):
#         self.title = title


# book1 = Book("Кобзар")
# book2 = Book("Лісова пісня")
# print(book1, book2)


# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price


# book1 = Book("Кобзар", 450)
# book2 = Book("Лісова пісня", 500)
# print("Перша:", book1.title, book1.price)
# print("Друга:", book2.title, book2.price)


# class Book:
#     def __init__(self, title, price, copies):
#         self.title = title
#         self.price = price
#         self.copies = copies


# book1 = Book("Кобзар", 450, 15)
# book2 = Book("Лісова пісня", 500)
# # print("Перша:", book1.title)
# # print("Перша книга вартість:", book1.price)
# # print("Друга:", book2.title, book2.price)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)
        
    def area(self):
        return self.width * self.height

    def info(self):
        print(f'Розміри прямокутника {self.width}x{self.height}')
        print(f'S={self.area()}')
        print(f'P={self.perimeter()}')


rect = Rectangle(5, 10)
rect.info()
