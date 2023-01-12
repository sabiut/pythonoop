class OperatingSystem:
    def __init__(self):
        self.os_type = ["Mac OS", "Windows OS", "Linux OS"]


class HP:
    website = "www.hp.com"
    name = "HP"


class ProBook(OperatingSystem, HP):
    def __init__(self):
        super().__init__()
        print("This is a {} machine and it is running {} ".format(self.name, self.os_type[1]))


pro_book = ProBook()
