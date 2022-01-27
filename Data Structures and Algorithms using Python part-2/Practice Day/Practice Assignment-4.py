"""
Problem Statement
The RS Exports company, in Bangalore, wants to deliver various goods such as television, microwave 
ovens, mixers, sofa set, chairs and computer tables, to its warehouse located in Chandigarh.

The mode of transport they prefer is railways. But there are no trains connecting Bangalore and 
Chandigarh. So they have planned to send the goods by train1 to Mumbai, where the goods would then be 
sent to Chandigarh by train2.

The following goods have been brought to the railway station for transport:

Product	television	microwave	mixers	sofaset	chairs	computertables
Quantity	26	        15        20	   5	  12	      5
The goods have to be arranged one after the other in a line, the product at the front of the line 
will be the first one to be loaded to the train.
Create a Goods class to represent Goods. Represent the goods_list using an appropriate data structure. 
Consider television as the first product in the goods_list.
"""
# lex_auth_0127716946325422081069

"""*********************Queue*****************************"""


class Queue:
    def __init__(self, max_size):

        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if self.__rear == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full!!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__front
        while index <= self.__rear:
            msg.append((str)(self.__elements[index]))
            index += 1
        msg = " ".join(msg)
        msg = "Queue data(Front to Rear): " + msg
        return msg


# Start writing your solution here
class Goods:
    def __init__(self, product, quantity):
        self.__product = product
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def __str__(self):
        return self.__product + ":" + str(self.__quantity)


goods_list = Queue(6)
goods_list.enqueue(Goods("television", 26))
goods_list.enqueue(Goods("microwave", 15))
goods_list.enqueue(Goods("mixers", 20))
goods_list.enqueue(Goods("sofaset", 5))
goods_list.enqueue(Goods("chairs", 12))
goods_list.enqueue(Goods("computertables", 5))
goods_list.display()
