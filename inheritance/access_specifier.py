
# naming convention of the access specifier
"""
Public-> member_name
Protected-> _member_name
Private-> __member_name
"""


class Fruits:
    fruits = ["mango", "orange", "banana", "pawpaw"]
    _color = ["yellow", "green"]
    __green_yellow = {"ripe": "yellow", "unripe": "green"}


class DisplayDetails(Fruits):
    """
    In python when a private specifier is defined in a class it can only be
    accessible within that class.
    When we derive a class that inherited the base class, the private
    specifier that we had define in the base class
    will not be accessible within our derive class.

    In our example we had define Fruits as our base class and our child class
    is DisplayDetails which inherited the Fruits class
    if we try to access __green_yellow from DisplayDetails(Fruits) our program
    will throw and error because  __green_yellow was define as private.
    it can only be accessible within the Fruits class

    """

    def display(self):
        try:
            print("Enter 0 or 1")
            userChoice = int(input())
            if userChoice == 0:
                if self._color[userChoice] == self.__green_yellow.get("ripe"):
                    print("The {} is ripe".format(self.fruits[0]))
            elif userChoice == 1:
                if self._color[userChoice] == self.__green_yellow.get("unripe"):
                    print("The {} is ripe".format(self.fruits[1]))
        except:
            print("__green_yellow is define as a private member for the base\
                 class Fruits.\n"
                  "It is not accessible from the derive class DisplayDetails")


class HackAroundPrivateMember(Fruits):
    """
python stores the private member __green_yellow as _Fruits__green_yellow.
A hack around this is to access it using the way python has store it.
But this is not regarded as good programming practice, so it is not encouraged
    """

    def notEncouraged(self):
        try:
            print("Enter 0 or 1")
            userChoice = int(input())
            if userChoice == 0:
                if self._color[userChoice] == self._Fruits__green_yellow.get("ripe"):
                    print("The {} is ripe".format(self.fruits[0]))
            elif userChoice == 1:
                if self._color[userChoice] == self._Fruits__green_yellow.get("unripe"):
                    print("The {} is ripe".format(self.fruits[1]))
        except:
            print("This is not encourage, its bad programming practice.\n")


display = DisplayDetails()
display.display()
# hackaroundit = HackAroundPrivateMember()
# hackaroundit.notEncouraged()


"""
A protected access specifier can only be used within the base class and
the derive class which inherited the base class
even though you can call it outside the class. The protected naming convention
is use to tell a developer that it is a
protected specifier and it is a member of the base and derive class and
can only be use within.
"""

#print(display._color)
# print(display._Fruits__green_yellow)

#https://realpython.com/oop-in-python-vs-java/#public-and-private