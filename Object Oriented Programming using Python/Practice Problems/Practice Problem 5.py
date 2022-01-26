"""
A garment ware house wants to automate its order taking and delivery process.
Write a python program to implement the class diagram given below.



Class description:
    1. garment_dict: Static dictionary which stores cloth type (key) and a list (value) which contains the number of pieces available, price per piece and number of days it would take to deliver it. Initialize it using the sample data given: {"shirt":[45,400,30],"trousers":[250,500,25],"saree":[500,750,10],"jersey": [750,200,5]}
    2. Constructor: Initialize attribute, order_date to today's date. (Hint: time.strftime("%d/%m/%Y") returns today's date in the provided string format)
    3. calculate_amount(): Calculate and return the total amount to be paid based on the cloth type and number of pieces ordered
    4. update_stock(): Update stock based on details given below.
        - Set the attribute, delivery_date to order_date + number of days required to deliver the ordered item. Hint: d = date.today() + timedelta(days=n) will give the resultant date which is the sum of today's date and 'n' number of days. Convert it to string using time.strftime("%d/%m/%Y") where time is the datetime variable to be converted to string.
        - Update the number of pieces available for the ordered cloth type based on number of pieces ordered
    5. take_order(): Take the order, calculate amount and update stock based on rules given below.
        a. If the ordered cloth type and quantity (no_of_piece) are available based on details in garment_dict
            - Calculate amount
            - Update stock
            - Return the calculated amount
        b. Else, return -1

Perform case sensitive string comparison.
Create an objects of GarmentOrder class, invoke take_order() method on the GarmentOrder objects, display the details and test your program.
"""

import time
from datetime import date, timedelta


class GarmentOrder:
    garment_dict = {
        "shirt": [45, 400, 30],
        "trousers": [250, 500, 25],
        "saree": [500, 750, 10],
        "jersey": [750, 200, 5],
    }

    def __init__(self, no_of_piece, cloth_type):
        self.__order_date = time.strftime("%d/%m/%Y")
        self.__cloth_type = cloth_type
        self.__no_of_piece = no_of_piece
        self.__delivery_date = None

    def calculate_amount(self):
        return GarmentOrder.garment_dict[self.__cloth_type][1] * self.__no_of_piece

    def update_stock(self):
        self.__delivery_date = date.today() + timedelta(
            days=GarmentOrder.garment_dict[self.__cloth_type][2]
        )
        self.__delivery_date = self.__delivery_date.strftime("%d/%m/%Y")
        GarmentOrder.garment_dict[self.__cloth_type][0] -= self.__no_of_piece

    def take_order(self):
        if (
            self.__cloth_type in GarmentOrder.garment_dict
            and GarmentOrder.garment_dict[self.__cloth_type][0] >= self.__no_of_piece
        ):
            self.update_stock()
            return self.calculate_amount()
        return -1

    def get_cloth_type(self):
        return self.__get_cloth

    def get_no_of_piece(self):
        return self.__no_of_piece

    def get_order_date(self):
        return self.__order_date

    def get_delivery_date(self):
        return self.__delivery_date


customer = GarmentOrder(3, "shirt")
print(customer.take_order())
