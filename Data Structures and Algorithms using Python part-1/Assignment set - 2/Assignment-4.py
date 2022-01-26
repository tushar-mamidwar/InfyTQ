"""
Problem Statement
The owner of a BakeHouse wants to keep track of the tables that are occupied in his cafe. Assume 
that there are 10 tables in his cafe numbered from 1 to 10. As and when a table is occupied, it 
must be added to the occupied_table_list and when a customer leaves, the corresponding table must 
be removed from the list.

Write a python program to implement BakeHouse class. Represent occupied_table_list using an 
appropriate data structure.

Note: Table numbers should be maintained in ascending order in the occupied_table_list.

Tables should be allocated and de-allocated as mentioned in the example below:
Example: Suppose tables 1, 2, 3 and 4 are initially allocated. Now if a new customer arrives, 
he should be allocated table 5 and the table list should be accordingly updated. If now customer 
at table 2 leaves, table list should be accordingly updated and the next new customer should be 
allocated table 2 as it is the first free table.

Implement the allocation logic in allocate_table() method and de-allocation logic in 
deallocate_table() method.
"""

# lex_auth_0127438800232038401622


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


class BakeHouse:
    def __init__(self):
        self.__occupied_table_list = LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list

    def allocate_table(self):
        current_node = self.__occupied_table_list.get_head()
        for i in range(1, 11):
            if self.__occupied_table_list.find_node(i) == None:
                if current_node == None:
                    self.__occupied_table_list.add(i)
                    return
                elif current_node.get_next() == None:
                    if current_node.get_data() > i:
                        self.__occupied_table_list.insert(i, None)
                        return
                    else:
                        self.__occupied_table_list.insert(i, current_node.get_data())
                        return
                elif self.__occupied_table_list.get_tail().get_data() < i:
                    self.__occupied_table_list.insert(
                        i, self.__occupied_table_list.get_tail().get_data()
                    )
                    return
                else:
                    if current_node.get_data() > i:
                        self.__occupied_table_list.insert(i, None)
                        return
                    previous_node = None
                    while current_node.get_data() < i:
                        previous_node = current_node
                        current_node = current_node.get_next()
                    self.__occupied_table_list.insert(i, previous_node.get_data())
                    return

    def deallocate_table(self, table_number):
        self.__occupied_table_list.delete(table_number)


bakehouse = BakeHouse()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.allocate_table()
bakehouse.get_occupied_table_list().add(7)
bakehouse.allocate_table()
bakehouse.get_occupied_table_list().display()
bakehouse.deallocate_table(2)
print()
bakehouse.get_occupied_table_list().display()
# Invoke the methods of BakeHouse class and test the program
