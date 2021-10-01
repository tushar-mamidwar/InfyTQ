"""
Problem Statement


Spice Hut is a tiffin service provider which home delivers dinner to their customers – Occasional customers and Regular customers.
Write a Python program to implement class diagram given below.

Class Description:
OccasionalCustomer class:
    1. Initialize static variable counter to 1000
    2. Inside the constructor, auto-generate bill_id starting from 1001 prefixed by "O"
    3. validate_distance_in_kms(): Validate distance in kms
        a. Delivery distance in kms should be between 1 and 5 (both inclusive)
        b. If so, return true. Else, return false

Distance in kms                                 Delivery charge in Rs.
Between 1 and 2(both inclusive)                     Rs. 5 per km
Between 2 and 5(excluding 2,including 5)           Rs. 7.5 per km

    4. calculate_bill_amount(): Calculate total bill amount
        a. Validate distance in kms
        b. If valid, compute bill amount based on details mentioned below
            - Occasional customers can order only one tiffin per person
            - Cost/tiffin is Rs. 50
            - Delivery charges based on distance is as mentioned in the table
            - Bill amount includes tiffin cost and delivery charge
            - Set attribute, bill_amount with the computed bill amount value and return it
        c. If invalid, set attribute, bill_amount as -1 and return it

RegularCustomer class:
    1. Initialize static variable counter to 100
    2. Inside the constructor, auto-generate bill_id starting from 101 prefixed by "R"
    3. validate_no_of_tiffin(): Validate number of tiffins
        a. Regular customer can order a min of 1 and a max of 7 tiffins
        b. If value of no_of_tiffins is valid, return true. Else, return false
    4. calculate_bill_amount(): Calculate weekly bill amount
        a. Validate number of tiffins
        b. If valid, compute bill amount based on details mentioned below
            - Cost/tiffin is Rs. 50
            - The order is applicable for all the 7 days of a week
            - Compute the bill amount based on cost/tiffin, number of tiffins and number of days
            - Set attribute, bill_amount with the computed bill amount value and return it
        c. If invalid, set attribute, bill_amount as -1 and return it

Note: Perform case sensitive string comparison

For testing:
- Create objects of OccasionalCustomer and RegularCustomer classes
- Invoke calculate_bill_amount() on OccasionalCustomer and RegularCustomer objects
- Display the details of the customer
"""
from abc import ABCMeta, abstractmethod


class Customer(metaclass=ABCMeta):
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.bill_amount = None
        self.bill_id = None

    @abstractmethod
    def calculate_bill_amount(self):
        pass

    def get_customer_name(self):
        return self.__customer_name


class OccasionalCustomer(Customer):
    __counter = 1000

    def __init__(self, distance_in_kms, customer_name):
        super().__init__(customer_name)
        OccasionalCustomer.__counter += 1
        self.bill_id = 'O' + str(OccasionalCustomer.__counter)
        self.__distance_in_kms = distance_in_kms

    def get_distance_in_kms(self):
        return self.__distance_in_kms

    def validate_distance_in_kms(self):
        if 1 <= self.__distance_in_kms <= 5:
            return True
        return False

    def calculate_bill_amount(self):
        if self.validate_distance_in_kms():
            self.__bill_amount = 50
            if self.__distance_in_kms <= 2:
                self.__bill_amount += self.__distance_in_kms * 5
            else:
                self.__bill_amount += self.__distance_in_kms * 7.5
            return self.__bill_amount
        else:
            self.__bill_amount = -1
            return -1


class RegularCustomer(Customer):
    __counter = 100

    def __init__(self, no_of_tiffin, customer_name):
        super().__init__(customer_name)
        RegularCustomer.__counter += 1
        self.bill_id = 'R' + str(RegularCustomer.__counter)
        self.__no_of_tiffin = no_of_tiffin

    def validate_no_of_tiffin(self):
        if 1 <= self.__no_of_tiffin <= 7:
            return True
        return False

    def calculate_bill_amount(self):
        if self.validate_no_of_tiffin():
            self.bill_amount = 50 * 7 * self.__no_of_tiffin
            return self.bill_amount
        self.bill_amount = -1
        return -1

    def get_no_of_tiffin(self):
        return self.__no_of_tiffin


cus1 = RegularCustomer(2, "cus1")
print(cus1.calculate_bill_amount())
cus2 = OccasionalCustomer(4, "Cus2")
print(cus2.calculate_bill_amount())
