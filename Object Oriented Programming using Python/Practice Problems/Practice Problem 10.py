"""
An IT major wants to automate their process of employee laptop verification. A laptop allocated to
an employee has a QR code and allocation expiry status. There will be only one laptop allocated to
each employee.

Write a python program to implement the class diagram given below.

Class description:
Laptop:
    1. qrcode: Unique identity code of a laptop
    2. expiry: Boolean value which indicates the allocation expiry status of the laptop.
       True – allocation has expired, False – allocation has not expired

Scanner:
    1. emp_laptop_dict: Dictionary which stores employee id as key and corresponding laptop object as value
    2. scan(empid,laptop): Accept the employee id and laptop that needs to be scanned.
        a. Check if the given employee is allocated the given laptop
            - If the laptop allocation has not expired, return true. Else return false
        b. Else return false

Perform case sensitive string comparison.

Create few objects of Laptop class, use it to initialize emp_laptop_dict and create an object of
Scanner class using the emp_laptop_dict.

Invoke scan(empid, laptop) on Scanner object by passing different empid and laptops and test your program.

"""


class Laptop:
    def __init__(self, grcode, expiry):
        self.__grcode = grcode
        self.__expiry = expiry

    def get_grcode(self):
        return self.__grcode

    def get_expiry(self):
        return self.__expiry


class Scanner:
    def __init__(self, emp_laptop_dict):
        self.__emp_laptop_dict = emp_laptop_dict

    def scan(self, empid, laptop):
        if empid in self.__emp_laptop_dict:
            if not laptop.get_expiry():
                return True
            return False
        return False
