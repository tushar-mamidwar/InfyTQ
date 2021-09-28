"""
In the retail store scenario, let's look at the portion of customer purchasing items from the retail store.



Write a python program to implement the class diagram given below.



Class Description:

Bill class:

    1.Initialize static variable counter to 1000
    2.generate_bill_amount(item_quantity,items): Calculate bill amount based on the items purchased by the customer
        a. Accept a dictionary, item_quantity which contains the item id (key) of the items purchased along
           with the quantity (value)
        b. Accept a list, items which contains the list of Item objects available in the store
        c. Generate bill id starting from 1001 prefixed by "B" and initialize attribute,
           bill_id. Ex. "B1001", "B1002" etc.
        d. Calculate bill amount based on the quantity and price of the items purchased by the customer
        e. Set attribute, bill_amount with the calculated bill amount
Assume that values in item_quantity and items are always valid.
Customer class:

pays_bill(bill): Pay bill based on the bill amount
    a. Accept Bill object which contains the details of the bill to be paid by the customer
    b. Update attribute, payment_status to "Paid"
    c. Display customer name, bill id and bill amount
Note: Perform case insensitive string comparison

For testing:

- Create objects of Customer class, Item class and Bill class
- Invoke generate_bill_amount(item_quantity,items) on Bill object by passing the dictionary containing
  item_id and quantity of items purchased by the Customer and list of Item objects
- Invoke pays_bill() on Customer object by passing the Bill object
"""


class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name
        self.__payment_status = None

    def pays_bill(self, bill):
        self.__payment_status = "Paid"
        print(self.__customer_name, bill.get_bill_id(), bill.get_bill_amount())

    def get_customer_name(self):
        return self.__customer_name

    def get_payment_status(self):
        return self.__payment_status


class Bill:
    counter = 1000

    def __init__(self):
        self.__bill_id = None
        self.__bill_amount = 0

    def generate_bill_amount(self, item_quantity, items):
        for item_id in item_quantity:
            for item in items:
                if item_id.lower() == item.get_item_id().lower():
                    self.__bill_amount += item_quantity[item_id] * item.get_price_per_quantity()
        Bill.counter += 1
        self.__bill_id = 'B' + str(Bill.counter)

    def get_bill_id(self):
        return self.__bill_id

    def get_bill_amount(self):
        return self.__bill_amount


class Item:
    def __init__(self, item_id, description, price_per_quantity):
        self.__item_id = item_id
        self.__description = description
        self.__price_per_quantity = price_per_quantity

    def get_item_id(self):
        return self.__item_id

    def get_description(self):
        return self.__description

    def get_price_per_quantity(self):
        return self.__price_per_quantity


cus1 = Customer("cus1")
item1 = Item(123, "cake", 20)
item2 = Item(124, "pastry", 35)
item3 = Item(125, "bread", 20)
item4 = Item(126, "toast", 30)
bill1 = Bill()
bill1.generate_bill_amount({123: 3, 125: 4, 126: 2}, [item1, item2, item3, item4])
cus1.pays_bill(bill1)
