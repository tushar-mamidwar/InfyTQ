"""
Problem Statement
Represent the trains to transport the goods as per the details given below: Train1 (Lokmanya) travels 
from Bangalore to Mumbai and train2 (Rajdhani) travels from Mumbai to Chandigarh. The passenger capacity 
of each compartment of train1 and train2 are 60 and 75 respectively.
Consider Passenger to Goods ratio as 5 : 1 for both train1 and train2.
(i.e., 
Case 1: Compartment having only passengers or goods.
    Train1 can accomodate either 60 passengers or 12 goods in every compartment and 
    train2 can accomodate either 75 passengers or 15 goods in every compartment.
Case 2: Compartment having both passengers and goods.
    In train1, suppose there are 30 passengers in a compartment, then it can accomodate 6 goods and
    in train2, suppose there are 40 passengers in a compartment, then it can accomodate 7 goods) 
Note: Passenger to Goods ratio can be initialized as 5 in the program.

Create a Train class as shown below, represent train1 and train2 and display its details:
"""

# lex_auth_0127717001465856001076

# Start writing your solution here
class Train:
    def __init__(
        self,
        train_name,
        source,
        destination,
        passenger_capacity_per_compartment,
        passenger_goods_ratio,
    ):
        self.__train_name = train_name
        self.__source = source
        self.__destination = destination
        self.__passenger_capacity_per_compartment = passenger_capacity_per_compartment
        self.__passenger_goods_ratio = passenger_goods_ratio

    def get_train_name(self):
        return self.__train_name

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def get_passenger_capacity_per_compartment(self):
        return self.__passenger_capacity_per_compartment

    def get_passenger_goods_ratio(self):
        return self.__passenger_goods_ratio

    def __str__(self):
        pass
