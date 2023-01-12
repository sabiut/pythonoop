class Plants:
    def __init__(self):
        self.plant_type = None

    def public(self):
        self.plant_type = ["coconuts", "mango", "banana"]

    def _color(self):
        self._color = ["yellow", "green"]


class DisplayPlanInfo(Plants):
    pass


"""
python stores the private member __green_yellow as _Fruits__green_yellow.
A hack around this is to access it using the way python has store it.
But this is not regarded as good programming practice, so it is not encouraged
"""


plants = Plants()
plants.public()
