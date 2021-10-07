"""
Problem Statement
A mobile shop wants to create an online application to sell mobile phones.
Write a python program to implement the class diagram given below.



Class description
OnlinePortal class:

    1. item_list: Static list which contains the list of names of phones that are sold using the
       online portal
    2. quantity_list: Static list which contains the quantity of each item
    3. price_list: Static list which contains the price of each item
    4. The above three lists have one-to-one correspondence
    5. search_item(item): Search for the given item in item_list. If found, return the index position
       of the item. Else return -1
    6. place_order(index,emi,quantity): Accept index position of the item being ordered, emi
       (True or False) and quantity and place order based on details given below:
         a. Update the quantity of the item in quantity_list
         b. Calculate the total cost of the item based on price in price_list and quantity ordered
         c. If the buyer has opted for emi, add 2% interest of total cost. Else provide 2% discount
            on total cost
         d. Return the final cost
    7. add_stock(item_name,quantity): Add stock for the given item based on rules mentioned below.
        a. Check if the given item is present in item_list.
        b. If found, check if the existing quantity of given item is less than or equal to 10. If so,
           add the given quantity to the existing stock. Else return -1
        c. Else return -2
    8. add_item(item_name,price,quantity): Add the given new item to the stock.
        a. Check if the given item is present in item_list. If not, append item_name, price and
           quantity to the appropriate static lists of the class
        b. If present, return -2

Buyer class:
    purchase(item_name,quantity,emi): Purchase the given item from Online portal based on details given below.
        1. Check if the given item is present in OnlinePortal
        2. If present, check if the required quantity is available.
            a. If so, place the order by invoking the appropriate method of OnlinePortal class and
               return the cost
            b. Else, return -1
        3. Else, return -2

Perform case sensitive comparison.
Create objects of Buyer, OnlinePortal classes, invoke appropriate methods and test your program.

"""


class OnlinePortal:
    item_list = []
    quantity_list = []
    price_list = []

    @staticmethod
    def search_item(item):
        if item in OnlinePortal.item_list:
            return OnlinePortal.item_list.index(item)
        return -1

    @staticmethod
    def place_order(index, emi, quantity):
        OnlinePortal.quantity_list[index] -= quantity
        total_cost = OnlinePortal.price_list[index] * quantity
        if emi:
            total_cost *= 1.02
        else:
            total_cost *= 0.98
        return total_cost

    @staticmethod
    def add_stock(item_name, quantity):
        if item_name in OnlinePortal.item_list:
            index = OnlinePortal.item_list.index(item_name)
            if OnlinePortal.quantity_list[index] <= 10:
                OnlinePortal.quantity_list[index] += quantity
                return
            return -1
        return -2

    @staticmethod
    def add_item(item_name, price, quantity):
        if not item_name in OnlinePortal.item_list:
            OnlinePortal.item_list.append(item_name)
            OnlinePortal.price_list.append(price)
            OnlinePortal.quantity_list.append(quantity)
            return
        return -2


class Buyer(OnlinePortal):
    def __init__(self, name, email_id):
        self.__name = name
        self.__email_id = email_id

    def get_name(self):
        return self.__name

    def get_email_id(self):
        return self.__email_id

    def purchase(self, item_name, quantity, emi):
        index = OnlinePortal.search_item(item_name)
        if index != -1:
            if OnlinePortal.quantity_list[index] >= quantity:
                return OnlinePortal.place_order(index, emi, quantity)
            return -1
        return -2
