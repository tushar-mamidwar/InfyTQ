"""
Problem Statement
Write a python function which accepts two sorted stacks and returns a new stack containing all the elements 
of input stacks in sorted order.

Note: The output stack should be of the size as that of the sum of the sizes of the input stacks. 

Sample Input                                    Expected Output

Stack1 (top - bottom): 7,6,5
Stack2 (top - bottom): 3,2,1                Stack (top-bottom) : 7,6,5,3,2,1

Stack1 (top - bottom): 15,10,3
Stack2 (top - bottom): 21,9,7               Stack (top-bottom) : 21,15,10,9,7,3
"""

# lex_auth_0127667360846643203336


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


def merge_stack(stack1, stack2):
    # Remove pass and write your logic here
    temp_stack1 = Stack(stack1.get_max_size() + stack2.get_max_size())
    temp_stack2 = Stack(temp_stack1.get_max_size())
    while not stack1.is_empty() and not stack2.is_empty():
        num1 = stack1.pop()
        num2 = stack2.pop()
        if num1 >= num2:
            temp_stack1.push(num1)
            stack2.push(num2)
        elif num1 < num2:
            temp_stack1.push(num2)
            stack1.push(num1)
    while not stack1.is_empty():
        num = stack1.pop()
        temp_stack1.push(num)
    while not stack2.is_empty():
        num = stack2.pop()
        temp_stack1.push(num)
    while not temp_stack1.is_empty():
        temp_stack2.push(temp_stack1.pop())
    return temp_stack2


# Pass different values to the function and test your program
stack2 = Stack(3)
stack2.push(9)
stack2.push(11)
stack2.push(15)

stack1 = Stack(4)
stack1.push(3)
stack1.push(7)
stack1.push(10)
stack1.push(21)

print("The elements in stack1 are:")
stack1.display()
print("The elements in stack2 are:")
stack2.display()
print()
output_stack = merge_stack(stack1, stack2)
print("The elements in the output stack are:")
output_stack.display()
