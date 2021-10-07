"""
A toll booth on the way to Bangalore wants to keep the track of the number of vehicles passed
through it and total amount collected by them.
Write a python program to implement the class diagram given below.

Class description:
Constructor: Initialize both the instance variables, no_of_vehicle, total_amount to 0

    1. count_vehicle(): Increment total number of vehicle by 1
    2. calculate_amount(vehicle_type): Accept vehicle type and identify toll amount for that vehicle
       based on details given in the table. Add it to the total_amount instance variable.
    3. collect_toll(owner_type,vehicle_type): Accept owner type and vehicle type of the vehicle for
       which toll should be collected.
       If the owner of the vehicle is a "VIP", then toll amount need not be collected but number of vehicles
       should be updated.
       For any other type of owner, calculate the toll amount and update the number of vehicles.
       (Hint: Invoke appropriate methods to complete the functionality)


    vehicle Type                Amount
        Car                       70
        Bus                       100
        Truck                     150
        Any other type            70
        of vehicle



Perform case insensitive string comparison.
Create an object of Tollbooth class, invoke collect_toll() method for different vehicles and test your program.


"""


class Tollbooth:
    def __init__(self):
        self.__no_of_vehicle = 0
        self.__total_amount = 0

    def calculate_amount(self, vehicle_type):
        price_dict = {"Car": 70, "Bus": 100, "Truck": 150}
        vehicle_type = vehicle_type.title()
        if vehicle_type in price_dict:
            self.__total_amount += price_dict[vehicle_type]
        else:
            self.__total_amount += 70

    def count_vehicle(self):
        self.__no_of_vehicle += 1

    def collect_toll(self, owner_type, vehicle_type):
        if owner_type.upper() != "VIP":
            self.calculate_amount(vehicle_type)
        self.count_vehicle()

    def get_no_of_vehicle(self):
        return self.__no_of_vehicle

    def get_total_amount(self):
        return self.__total_amount


vehicle = Tollbooth()
vehicle.collect_toll("VI", "car")
print(vehicle.get_total_amount(), vehicle.get_no_of_vehicle())
