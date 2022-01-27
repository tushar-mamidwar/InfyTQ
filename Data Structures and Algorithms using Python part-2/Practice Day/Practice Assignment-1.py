"""
Problem Statement
Given a queue of numbers. Write a python function to push every second element in the queue to a stack, 
if it is the triangle number of the previous element in the queue and return the stack. The output 
stack should be of the same size as that of the input queue.

Number d is said to be a triangle number of n, if d = 1 + 2 + 3 +….+ (n-2) + (n-1) + n.

For example, 28 is said to be the triangle number of 7, if 1+2+3+4+5+6+7 is equal to 28.

Sample Input	Expected Output
Input queue (front->rear): 7,28,8,35,3,6,5,15,2,5	
Output stack ( top->bottom): 15,6,28
"""
# lex_auth_01275171237137612864

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


def check_triangle_number(queue1):
    # Remove pass and write your logic here
    count = 1
    num = None
    output_stack = Stack(queue1.get_max_size() // 2)
    while not queue1.is_empty():
        num1 = queue1.dequeue()
        num2 = queue1.dequeue()
        if num2 == num1 * (num1 + 1) // 2:
            output_stack.push(num2)
    return output_stack


# Pass different values of queue to the function and test your program
queue1 = Queue(10)
queue1.enqueue(7)
queue1.enqueue(28)
queue1.enqueue(8)
queue1.enqueue(35)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(5)
queue1.enqueue(15)
queue1.enqueue(2)
queue1.enqueue(3)
print("The elements in the queue are:")
queue1.display()
check_triangle_number(queue1).display()
