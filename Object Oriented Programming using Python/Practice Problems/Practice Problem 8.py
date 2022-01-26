"""
Problem Statement
\
"Mysore cabs" wants to automate their booking service.
Write a python program to implement the class diagram given below.

Class description
CabRepository:
    1. Initialize static lists, cab_type_list, charge_per_km and no_of_cars using the sample data
       given in the table
    2. There is one to one correspondence between these static lists

        Cab type list       Hatch Back       Sedan        SUV
        Charge per km           9             12           5
        Number of cars          2             5            10

CabService:
    1. check_availability(): Check whether the requested cab type is available or not for booking by
       checking in CabRepository.cab_type_list. If available return index position of the cab type in
       CabRepository.cab_type_list. Else return -1
    2. get_cab_charge(index): Find and return the charge per km for the car at the given index position
       from CabRepository.charge_per_km list
    3. calculate_waiting_charge( waiting_time_mins): Calculate and return waiting charge based on the
       given waiting_time_mins
        1. For first 30 minutes there is no waiting charge
        2. After 30 minutes, 5 rupees should be charged for every extra minute
    4. booking(waiting_time_mins): Calculate and return the final amount to be paid by the customer
       including the waiting charge for given waiting_time_mins. Also update the number of available
       cars and generate the service id for each booking starting from 1001. Return -1 if the car is
       not available.

Perform case sensitive string comparison.

Create objects of CabService class. Invoke booking() on CabService class by passing waiting time in mins
and display the details.


"""


class CabRepository:
    cab_type_list = ["Hatch Back", "Sedan", "SUV"]
    charge_per_km = [9, 12, 5]
    no_of_cars = [2, 0, 10]


class CabService:
    __counter = 1000

    def __init__(self, cab_type, distance_in_kms):
        self.__cab_type = cab_type
        self.__service_id = None
        self.__distance_in_kms = distance_in_kms

    def get_cab_type(self):
        return self.__cab_type

    def get_service_id(self):
        return self.__service_id

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def check_availability(self):
        if self.__cab_type in CabRepository.cab_type_list:
            index = CabRepository.cab_type_list.index(self.__cab_type)
            if CabRepository.no_of_cars[index] != 0:
                return index
            return -1
        return -1

    def get_cab_charge(self, index):
        return CabRepository.charge_per_km[index]

    def calculate_waiting_charge(self, waiting_time_mins):
        charge = 0
        if waiting_time_mins >= 30:
            charge = 5 * (waiting_time_mins - 30)
        return charge

    def booking(self, waiting_time_mins):
        index = self.check_availability()
        if index != -1:
            charge = self.get_cab_charge(index) * self.__distance_in_kms
            charge += self.calculate_waiting_charge(waiting_time_mins)
            CabService.__counter += 1
            self.__service_id = CabService.__counter
            CabRepository.no_of_cars[index] -= 1
            return charge
        return -1


cab = CabService("Sedan", 3)
print(cab.booking(31))
