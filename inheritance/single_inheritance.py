class Car:

    def __init__(self):
        self._color_type = "red"


class Pickup(Car):
    def __init__(self):
        super().__init__()  # super is used to call base class methods. we will cover super in next section.
        self.__type_of_wheel = ['Steel Wheels', 'Alloy Wheels', 'Chrome Wheels']

    def setColor(self, color):
        self._color_type = color

    def displayCarsSpec(self):
        print("The pickup color is {} and the type of wheels that pickup is using is {}".format(self._color_type,
                                                                                                self.__type_of_wheel[
                                                                                                    1]))


car = Pickup()
print("Would you like to pick another color? y/n")
userChoice = input()
if userChoice == 'y':
    print("Pick your favourite")
    colorType = input()
    car.setColor(colorType)
elif userChoice == 'x':
    quit()
car.displayCarsSpec()
