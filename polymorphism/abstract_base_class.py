from abc import ABC, abstractmethod

"""Abstract class is use to create blueprint for other classes. You cannot create object for an abstract class, 
in the same way the abstract method is a method without an implementation.
In python the module that provides the base for define the Abstract Base class is ABC.

To make a method abstract we can decorate it with @abstractmenthod

https://docs.python.org/3/library/abc.html
"""


class AbstractClass(ABC):

    @abstractmethod
    def A(self):
        pass

    @abstractmethod
    def B(self):
        pass

    @abstractmethod
    def C(self):
        pass


class ChildClass(AbstractClass):

    def A(self):
        print("test A")

    def B(self):
        print("test B")

    def C(self):
        print("test C")


ab = ChildClass()
ab.A()
