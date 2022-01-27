"""
Problem Statement
Each train has compartments which can be occupied by passengers and/or goods. The compartments of both 
the trains should be filled with the passengers first, based on the compartment capacity. The compartment 
names of both the trains should be auto generated whenever a new compartment is added. The compartment 
name should start with the first letter of the train name .ie. for train1(Lokmanya), it should begin 
with “L” and for train2(Rajdhani), it should begin with “R”. Eg: L0, L1…, R0, R1…

Create a Compartment class and modify the Train class to add the highlighted variables and methods.

Note: Use the code for Train class from Practice Assignment - 5.



The compartments are expected to be frequently added and removed based on need at each station and they 
need to be added to a train based on the number of passengers and goods. Consider compartment_list to 
be a linked list.

add_passenger_compartments(no_of_passengers) accepts number of passengers who have booked tickets for 
traveling by the train. This method should add compartments to the compartment_list based on the 
number of passengers and passenger capacity per compartment. Note: Assumption is that number of 
passengers should be a multiple of 5.

Note that based on number of passengers, it may happen that the last passenger compartment is not 
completely filled. Initialize number of passengers for each compartment and consider number of goods 
to be 0 in these compartments.

If there are 180 passengers waiting to board train1 and 110 passengers waiting for train2, 
invoke add_passenger_compartments() based on number of passengers for train1 and train2 and display 
the compartment details.
"""

# lex_auth_0127716999111884801080

"""*********************Linkedlist************************"""


class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def add(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail = new_node

    def insert(self, data, data_before):
        new_node = Node(data)
        if data_before == None:
            new_node.set_next(self.__head)
            self.__head = new_node
            if new_node.get_next() == None:
                self.__tail = new_node

        else:
            node_before = self.find_node(data_before)
            if node_before is not None:
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if new_node.get_next() is None:
                    self.__tail = new_node
            else:
                print(data_before, "is not present in the Linked list")

    def display(self):
        temp = self.__head
        while temp is not None:
            print(temp.get_data())
            temp = temp.get_next()

    def find_node(self, data):
        temp = self.__head
        while temp is not None:
            if temp.get_data() == data:
                return temp
            temp = temp.get_next()
        return None

    def delete(self, data):
        node = self.find_node(data)
        if node is not None:
            if node == self.__head:
                if self.__head == self.__tail:
                    self.__tail = None
                self.__head = node.get_next()
            else:
                temp = self.__head
                while temp is not None:
                    if temp.get_next() == node:
                        temp.set_next(node.get_next())
                        if node == self.__tail:
                            self.__tail = temp
                        node.set_next(None)
                        break
                    temp = temp.get_next()
        else:
            print(data, "is not present in Linked list")

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp = self.__head
        msg = []
        while temp is not None:
            msg.append(str(temp.get_data()))
            temp = temp.get_next()
        msg = " ".join(msg)
        msg = "Linkedlist data(Head to Tail): " + msg
        return msg


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
        self.__compartment_list = LinkedList()
        self.count = 0

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

    def get_compartment_list(self):
        return self.__compartment_list

    def add_passenger_compartments(self, no_of_passengers):
        while no_of_passengers >= self.__passenger_capacity_per_compartment:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count),
                self.__passenger_capacity_per_compartment,
                0,
            )
            no_of_passengers -= self.__passenger_capacity_per_compartment
            self.count += 1
            self.__compartment_list.add(new_compartment)
        if no_of_passengers != 0:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count), no_of_passengers, 0
            )
            self.count += 1
            self.__compartment_list.add(new_compartment)

    def __str__(self):
        pass


class Compartment:
    def __init__(self, name, no_of_passengers, no_of_goods):
        self.__name = name
        self.__no_of_passengers = no_of_passengers
        self.__no_of_goods = no_of_goods

    def get_name(self):
        return self.__name

    def get_no_of_passengers(self):
        return self.__no_of_passengers

    def get_no_of_goods(self):
        return self.__no_of_goods

    def __str__(self):
        pass
