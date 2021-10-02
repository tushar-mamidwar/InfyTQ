"""
Mega Mart, a retail shop, wants to record the number of items bought by its customers.

Write a python program to implement the class diagram given below.



Class Description:
    1. list_of_items: Static list which contains the list of items available in the store. Initialize it with sample data as given - [Cake, Soap, Jam, Cereal, Hand Sanitizer, Biscuits, Bread]
    2. list_of_count_of_each_item_sold: Static list which contains count of items sold. Initialize count of each item to 0
    3. The above two lists have one-to-one correspondence
    4. items_purchased: List which contains the list of items purchased by the customer. Initialize it to an empty list in the constructor
    5. item_on_offer: Name of the item provided as an offer. Initialize it to None in the constructor
    6. provide_offer(): The shop has decided to give 1 Hand sanitizer free if soap is bought by the customer
        a. Increment the count of hand sanitizer in list_of_count_of_each_item_sold by 1
        b. Update the instance variable, item_on_offer to "HAND SANITIZER"
    7. sell_items(list_of_items_to_be_purchased): Accept the list of items that are to be purchased by the customer
        a. For every item in list_of_items_to_be_purchased
            - Increment count of the item in the static list, list_of_count_of_each_item_sold by 1
            - Add the item to attribute, items_purchased list
        b. If soap is purchased by the customer, then provide the offer by invoking the appropriate method
    8. find_total_items_sold(): Return the total number of items sold by the shop

Note:
- Perform case insensitive string comparison
- Assume that customer purchases only 1 quantity of each item and an item will appear only once in the list, list_of_items_to_be_purchased

For testing:
- Create objects of Purchase class
- Invoke sell_items() on Purchase object by passing the list of items to be purchased by the customer
- Display the details
"""

class Purchase:
    list_of_items=['Apple', 'Biscuits', 'Chocolates', 'Jam', 'Butter', 'Milk', 'Soap', 'Hand Sanitizer']
    list_of_count_of_each_item_sold=[0,0,0,0,0,0,0,0]
    def __init__(self):
        self.__item_on_offer=None
        self.__items_purchased=[]
    def provide_offer(self):
        Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index("Hand Sanitizer")]+=1
        self.__item_on_offer= "Hand Sanitizer"
    def sell_items(self,list_of_items_to_be_purchased):
        for i in range(len(list_of_items_to_be_purchased)):
            list_of_items_to_be_purchased[i]=list_of_items_to_be_purchased[i].title()
            if list_of_items_to_be_purchased[i] in Purchase.list_of_items:
                Purchase.list_of_count_of_each_item_sold[Purchase.list_of_items.index(list_of_items_to_be_purchased[i])]+=1
                self.__items_purchased.append(list_of_items_to_be_purchased[i])

        if "Soap" in list_of_items_to_be_purchased:
            self.provide_offer()
    @staticmethod
    def find_total_items_sold():
        sum=0
        for i in Purchase.list_of_count_of_each_item_sold:
            sum+=i
        return sum
    def get_item_on_offer(self):
        return self.__item_of_offer
    def get_items_purchased(self):
        return self.__items_purchased
purchase1=Purchase()
purchase1.sell_items(['JAM', 'CHOcolates', 'Ghee', 'Soap'])
print(purchase1.get_item_of_offer())
