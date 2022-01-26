"""
Problem Statement
Fortune hotel wants to automate their daily activities such as check in and check out. There are
two types of rooms- Standard and Luxury. Free wifi is available in Luxury room and comfortable desk
is available in standard room.

Write a python program to implement the class diagram given below.


Class description
Customer class:
    1. Initialize static variable counter to 1000

Hotel class:
    1. room_list: List of objects of rooms in the hotel
    2. check_in(customer, room_type): Check-in the given customer based on details mentioned below.
        1. Customer can check in, only if the type of room desired by the customer is available.
        2. If the room is available,
            - Auto-generate room.customer.customer_id starting from 1001
            - Assign the customer to the available room
            - Return true
        3. Else, return false
    3. check_out(customer): Check-out the given customer based on details mentioned below.
        1. Find out the room allocated to the given customer. If found,
            - Identify the room rent based on type and number of days stayed by the customer
            - Release the room, i.e., the room should be available for check in by other customers.
            - Return total room rent
        2. Else, return false

Room class:
    1. Initialize static variable counter to 100
    2. Auto-generate room_id in the child class constructors starting from 101 and prefixed by
    "L" for luxury room and "S" for Standard room. Examples – S101, L102, S103, L104, L105 etc.

LuxuryRoom class:
    calculate_room_rent(no_of_days): Calculate room rent
        1. Calculate room rent based on room price and number of days
        2. For stay of more than 5 days, provide 5% discount on total room rent
        3. Return the final room rent

StandardRoom class:
    calculate_room_rent(no_of_days): Calculate room rent
        1. Calculate room rent based on room price and number of days
        2. Return the calculated room rent

Perform case sensitive comparison.

Create objects of Hotel class, invoke appropriate methods and test your program.
"""

from abc import ABCMeta, abstractmethod


class Customer:
    counter = 1000

    def __init__(self, customer_name, address, no_of_days):
        self.__customer_name = customer_name
        self.__address = address
        self.__no_of_days = no_of_days
        self.__customer_id = None

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_address(self, address):
        self.__address = address

    def set_no_of_days(self, no_of_days):
        self.__no_of_days = no_of_days

    def get_no_of_days(self):
        return self.__no_of_days

    def get_address(self):
        return self.__address

    def get_customer_name(self):
        return self.__customer_name

    def get_customer_id(self):
        return self.__customer_id


class Room(metaclass=ABCMeta):
    counter = 101

    def __init__(self, price):
        self.__price = price
        self.__room_id = None
        self.__customer = None

    def get_room_id(self):
        return self.__room_id

    def get_customer(self):
        return self.__customer

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def set_room_id(self, room_id):
        self.__room_id = room_id

    def set_customer(self, customer):
        self.__customer = customer

    @abstractmethod
    def calculate_room_rent(self, no_of_days):
        pass


class LuxuryRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        self.__free_wifi = True
        Room.counter += 1
        self.set_room_id("L" + str(Room.counter))

    def get_free_wifi(self):
        return self.__free_wifi

    def set_free_wifi(self, free_wifi):
        self.__free_wifi = free_wifi

    def calculate_room_rent(self, no_of_days):
        total_rent = self.get_price() * no_of_days
        if no_of_days > 5:
            total_rent *= 0.95
        return total_rent


class StandardRoom(Room):
    def __init__(self, price):
        super().__init__(price)
        Room.counter += 1
        self.set_room_id("S" + str(Room.counter))
        self.__comfortable_desk = True

    def get_comfortable_desk(self):
        return self.__comfortable_desk

    def set_comfortable_desk(self, comfortable_desk):
        self.__comfortable_desk = comfortable_desk

    def calculate_room_rent(self, no_of_days):
        return self.get_price() * no_of_days


class Hotel:
    def __init__(self, room_list, location):
        self.__room_list = room_list
        self.__location = location

    def get_room_list(self):
        return self.__room_list

    def set_room_list(self, room_list):
        self.__room_list = room_list

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def check_in(self, customer, room_type):
        for room in self.__room_list:
            if room.get_room_id()[0] == room_type[0] and room.get_customer() == None:
                room.set_customer(customer)
                Customer.counter += 1
                room.get_customer().set_customer_id(Customer.counter)

                return True
        return False

    def check_out(self, customer):
        for room in self.__room_list:
            if room.get_customer() != None:
                if room.get_customer().get_customer_id() == customer.get_customer_id():
                    room_rent = room.calculate_room_rent(
                        room.get_customer().get_no_of_days()
                    )
                    room.set_customer(None)
                    return room_rent
        return False


room = StandardRoom(6)
