class Person:
    # class attributes

    # constructor method
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    # instance method
    def displayPersonInfo(self):
        pass

    # instance method
    def whatPersonDoes(self):
        self.action = ["walk", "run", "cook"]

        # instance method

    def anotherMethod(self):
        self.whatPersonDoes()
        print(self.name, "can", self.action[2])


if __name__ == "__main__":
    person = Person("Ben", 20, "stree", 873645)
    person.anotherMethod()


class Person:

    def method1(self):
        pass

    def method2(self):
        pass

person = Person()
person.method1()


class Person:
    # class attributes

    # constructor method
    def __init__(self):
        pass

    # instance method
    def displayPersonInfo(self):
        pass

    # instance method
    def whatPersonDoes(self):
        pass

        # instance method

    def anotherMethod(self):
        pass


if __name__ == "__main__":
    pass
