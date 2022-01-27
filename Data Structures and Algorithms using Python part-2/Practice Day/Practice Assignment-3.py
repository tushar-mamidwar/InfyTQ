"""
Problem Statement
Write a python function to implement separate chaining technique for handling collision in a hash 
table. The function should accept the list of whole numbers that need to be hashed and the size of 
the hash table, n. It should store the whole numbers in the linked list at the appropriate index positions 
of the hash table and return the hash table.
Assume that the hash function is h(k)=k % n, where k is the number to hashed and n is the size of the 
hash table. 
Hint: Consider each element of the hash table to be a linked list. 
Example: hash_table[0]=LinkedList(), hash_table[1]=LinkedList() etc.
"""
# lex_auth_01275172328921497674

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


def separate_chaining(list_of_numbers, size_of_hash_table):
    # Remove pass and write your logic here
    hashed_list = [LinkedList() for i in range(size_of_hash_table)]
    for number in list_of_numbers:
        hashed_list[number % size_of_hash_table].add(number)
    return hashed_list


# Pass different values to the function and test your program
list_of_numbers = [81, 20, 34, 42, 21, 45, 33, 99]
size_of_hash_table = 5
result_hash_table = separate_chaining(list_of_numbers, size_of_hash_table)
count = 0
for k in result_hash_table:
    print("Values in hash table at index", count)
    count += 1
    k.display()
