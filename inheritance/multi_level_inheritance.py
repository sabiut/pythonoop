class OperatingSystem:
    def __init__(self):
        self.os_type = ["Mac OS", "Windows OS", "Linux OS"]


class HP(OperatingSystem):
    def __init__(self):
        super().__init__()
        self.detail = {"website": "www.hp.com", "name": "HP", "model": "ProBook"}


class ProBook(HP):
    def display(self):
        super().__init__()
        print("This is a {} machine and it is running {} ".format(self.detail.get("name"), self.os_type[1]))
        print("For more information visit {} ".format(self.detail.get("website")))


pro_book = ProBook()
pro_book.display()
