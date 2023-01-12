class Car:

    def __init__(self):
        self.car_list = {'pickup': 150, 'hatchback': 30, 'sedan': 80, 'suv': 100}

    def carInfo(self):
        print("\n")
        print("-----Car Rental Info-----")
        print("#############################################################")
        print("Pickup:", "$", self.car_list.get("pickup"), "per day")
        print("Hatchback:", "$", self.car_list.get("hatchback"), "per day")
        print("Sedan:", "$", self.car_list.get("sedan"), "per day")
        print("SUV:", "$", self.car_list.get("suv"), "per day")
        print("#############################################################")

    def rentalCost(self, car_type, num_of_days):
        total_rental_cost = self.car_list.get(car_type) * num_of_days
        return total_rental_cost
