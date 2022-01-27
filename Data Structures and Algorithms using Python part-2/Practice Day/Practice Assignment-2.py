"""
Problem Statement
Given a stack with strings, A through E, in alphabetical order with "A" on top.

Write a python function to accept the given stack and perform the following:

The bottom three elements should be simultaneously removed and placed on top with their vertical order 
maintained and it should return the updated input stack.
Input stack (top->bottom): A,B,C,D,E
Output stack (top->bottom) :C,D,E,A,B
"""
# lex_auth_01275171830954393670

"""*********************Stack*****************************"""


class Stack:
    def __init__(self, max_size):
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__top = -1

    def is_full(self):
        if self.__top == self.__max_size - 1:
            return True
        return False

    def is_empty(self):
        if self.__top == -1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("The stack is full!!")
        else:
            self.__top += 1
            self.__elements[self.__top] = data

    def pop(self):
        if self.is_empty():
            print("The stack is empty!!")
        else:
            data = self.__elements[self.__top]
            self.__top -= 1
            return data

    def display(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            index = self.__top
            while index >= 0:
                print(self.__elements[index])
                index -= 1

    def get_max_size(self):
        return self.__max_size

    # You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg = []
        index = self.__top
        while index >= 0:
            msg.append((str)(self.__elements[index]))
            index -= 1
        msg = " ".join(msg)
        msg = "Stack data(Top to Bottom): " + msg
        return msg


def stack_operation(input_stack):
    # Remove pass and write your logic here
    size = input_stack.get_max_size()
    temp_stack = Stack(size)
    bottom_3_stack = Stack(3)
    i = 0
    while i < size - 3:
        temp_stack.push(input_stack.pop())
        i += 1
    i = 0
    while i < 3:
        bottom_3_stack.push(input_stack.pop())
        i += 1
    while not temp_stack.is_empty():
        input_stack.push(temp_stack.pop())
    while not bottom_3_stack.is_empty():
        input_stack.push(bottom_3_stack.pop())
    return input_stack


# Pass different values of stack to the function and test your program
input_stack = Stack(5)
input_stack.push("E")
input_stack.push("D")
input_stack.push("C")
input_stack.push("B")
input_stack.push("A")

print("The elements in input stack are:")
input_stack.display()
print()
updated_stack = stack_operation(input_stack)
print("The elements in the updated stack are:")
updated_stack.display()
