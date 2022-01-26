"""
Problem Statement
An apparel shop wants to manage the items which it sells.
Write a python program to implement the class diagram given below.



Class Description:

Apparel class:
1. Initialize static variable counter to 100
2. In the constructor, auto-generate item_id starting from 101 prefixed by "C" for cotton apparels and "S" for silk apparels. Example – C101, S102, S103, C104 etc.
3. calculate_price(): Add 5% service tax on the price of the apparel and update attribute, price with the new value

Cotton class:
1. While invoking parent constructor from child constructor, pass "Cotton" as item_type
2. calculate_price(): Update attribute, price of Apparel class based on rules given below
    a. Add service tax on price by invoking appropriate method of Apparel class
    b. Apply discount on price
    c. Add 5% VAT on final price

Silk class:
1. While invoking parent constructor from child constructor, pass "Silk" as item_type
2. calculate_price(): Update attribute, price of Apparel class based on rules given below
    a. Add service tax on price by invoking appropriate method of Apparel class
    b. Identify points earned based on rules given below:
        - Silk apparels with price more than Rs. 10000, earn 10 points and anything less than or equal to that earn 3 points
    c. Initialize attribute, points with the identified points
    d. Add 10% VAT on price
Note: Perform case sensitive string comparison

For testing:

- Create objects of Cotton class and Silk class
- Invoke calculate_price() on Cotton objects and Silk objects
- Display their details
"""


class Apparel:
    counter = 100

    def __init__(self, price, item_type):
        Apparel.counter += 1
        self.__item_id = item_type[0] + str(Apparel.counter)
        self.__price = price
        self.__item_type = item_type

    def calculate_price(self):
        self.__price *= 1.05

    def get_item_id(self):
        return self.__item_id

    def get_item_type(self):
        return self.__item_type

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class Cotton(Apparel):
    def __init__(self, price, discount):
        self.__discount = discount
        super().__init__(price, "Cotton")

    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price -= self.get_discount()
        price *= 1.05
        self.set_price(price)

    def get_discount(self):
        return self.get_price() * self.__discount / 100


class Silk(Apparel):
    def __init__(self, price):
        self.__points = 0
        super().__init__(price, "Silk")

    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        if price > 10000:
            self.__points += 10
        else:
            self.__points += 3
        self.set_price(price * 1.1)

    def get_points(self):
        return self.__points


cotton = Cotton(340, 10)
silk = Silk(405)
cotton.calculate_price()
silk.calculate_price()
print(cotton.get_item_id(), cotton.get_item_type(), cotton.get_price())
print(silk.get_item_id(), silk.get_item_type(), silk.get_price())
