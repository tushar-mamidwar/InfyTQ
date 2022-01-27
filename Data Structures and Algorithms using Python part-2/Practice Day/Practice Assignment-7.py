"""
Problem Statement
Once the passengers are filled, goods should be filled one by one. The goods at the front of the line 
should be the first one to be moved into a compartment.Modify the Train class to add the highlighted 
method.

Note: Reuse the code for Compartment class, Goods class and Train class from Practice Assignment - 4 
and Practice Assignment - 6.
"""


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

    def add_goods(self, goods_list):
        total_goods = 0
        while not goods_list.is_empty():
            total_goods += goods_list.dequeue().get_quantity()
        goods_capacity = (
            self.__passenger_capacity_per_compartment // self.__passenger_goods_ratio
        )
        last_compartment = self.__compartment_list.get_tail().get_data()
        no_of_goods_vacant = (
            self.__passenger_capacity_per_compartment
            - last_compartment.get_no_of_passengers()
        ) // self.__passenger_goods_ratio
        if no_of_goods_vacant != 0:
            if no_of_goods_vacant <= total_goods:
                total_goods -= no_of_goods_vacant
                last_compartment.set_no_of_goods(no_of_goods_vacant)
            else:
                last_compartment.set_no_of_goods(total_goods)
                total_goods = 0
        while total_goods >= goods_capacity:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count), 0, goods_capacity
            )
            total_goods -= goods_capacity
            self.count += 1
            self.__compartment_list.add(new_compartment)
        if total_goods != 0:
            new_compartment = Compartment(
                self.__train_name[0] + str(self.count), 0, total_goods
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

    def set_no_of_goods(self, goods):
        self.__no_of_goods = goods

    def __str__(self):
        pass


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
