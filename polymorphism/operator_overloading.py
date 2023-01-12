"""
Python interprets the plus "+" operator  as __add__
when the "+" operator is used the special method __add__ is invoked
"""
print(3 + 2)
print(int.__add__(3, 2))


class Book:
    def __init__(self, price):
        self.price = price

    def __add__(self, other):
        return self.price + other.price


book1 = Book(30)
book2 = Book(23)
print("total:", book1 + book2)


# print(dir(Book))


class Fruits:
    def __init__(self):
        self.fruits = {"mango": 5.00, "apple": 1.00, "orange": 1.00}

    def __add__(self, other):
        return self.fruits.get("mango") + self.fruits.get("apple")


fruit1 = Fruits()
fruit2 = Fruits()
print(int(fruit1 + fruit2))
