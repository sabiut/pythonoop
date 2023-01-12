from car_rent import Car

rental_info = Car()

if __name__ == "__main__":
    while True:
        print("\n")
        print("Enter a to display the car rental information")
        print("Enter b to rent a car")
        print("Enter x to exit")
        customerOptions = input()
        if customerOptions == "a":
            rental_info.carInfo()
        elif customerOptions == "b":
            print("Please pick your car type")
            car_type = input()
            if car_type not in rental_info.car_list:
                print("Sorry this car is not available!")
            else:
                print("How many days are you planning on renting the car?")
                number_of_days = int(input())
                total_cost = rental_info.rentalCost(car_type, number_of_days)
                print("The total cost of renting a", car_type, "for", number_of_days, "days is", "$", total_cost)
                rental_info.car_list.pop(car_type)
        elif customerOptions == "x":
            quit()
