"""
Problem Statement
The TwinkleStar kindergarten kids are given a new game everyday to play among themselves. 
The teacher has come up with an idea for the kids to learn grouping and sorting. The teacher has 
given a container full of colored balls. Assume that the container has the following balls:

 Color	 Red	 Blue	 Yellow	 Blue	 Yellow	 Green	 Green	 Red
 Name	 A	       B	    B	  A	        A	   B	   A	  B

There are two each (A,B) of red, green ,blue and yellow balls in the container.
The task for the children is to take out the balls one at a time from the container and put it in 
four different containers based on the color. After that, the balls should be arranged such that 
the corresponding colored ball A is on top in all the four containers.

Note : The diameter of all the five containers are equal to that of a single ball, hence balls 
       should be arranged one on top of the other.

Use the Ball class and list of balls to implement the class Game as given in the class diagram.

1. In the constructor of Game class create lists to store balls of different color separately

2. Display the color and name of the balls before and after grouping and arranging them in order.

Note: You may use the appropriate data structure(s) for solving this problem 
"""

# lex_auth_0127438939341373441628


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


class Ball:
    def __init__(self, color, name):
        self.__color = color
        self.__name = name

    def __str__(self):
        return self.__color + " " + self.__name

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name


# Implement Game class here
class Game:
    def __init__(self, ball_stack):
        self.ball_container = ball_stack
        self.red_balls_container = Stack(2)
        self.green_balls_container = Stack(2)
        self.blue_balls_container = Stack(2)
        self.yellow_balls_container = Stack(2)

    def grouping_based_on_color(self):
        while not self.ball_container.is_empty():
            ball = self.ball_container.pop()
            if ball.get_color() == "Red":
                self.red_balls_container.push(ball)
            elif ball.get_color() == "Green":
                self.green_balls_container.push(ball)
            elif ball.get_color() == "Blue":
                self.blue_balls_container.push(ball)
            elif ball.get_color() == "Yellow":
                self.yellow_balls_container.push(ball)

    def rearrange_balls(self, color):
        if color == "Red":
            ball1 = self.red_balls_container.pop()
            ball2 = self.red_balls_container.pop()
            if ball1.get_name() == "A":
                self.red_balls_container.push(ball2)
                self.red_balls_container.push(ball1)
            else:
                self.red_balls_container.push(ball1)
                self.red_balls_container.push(ball2)
        elif color == "Green":
            ball1 = self.green_balls_container.pop()
            ball2 = self.green_balls_container.pop()
            if ball1.get_name() == "A":
                self.green_balls_container.push(ball2)
                self.green_balls_container.push(ball1)
            else:
                self.green_balls_container.push(ball1)
                self.green_balls_container.push(ball2)
        if color == "Blue":
            ball1 = self.blue_balls_container.pop()
            ball2 = self.blue_balls_container.pop()
            if ball1.get_name() == "A":
                self.blue_balls_container.push(ball2)
                self.blue_balls_container.push(ball1)
            else:
                self.blue_balls_container.push(ball1)
                self.blue_balls_container.push(ball2)
        if color == "Yellow":
            ball1 = self.yellow_balls_container.pop()
            ball2 = self.yellow_balls_container.pop()
            if ball1.get_name() == "A":
                self.yellow_balls_container.push(ball2)
                self.yellow_balls_container.push(ball1)
            else:
                self.yellow_balls_container.push(ball1)
                self.yellow_balls_container.push(ball2)

    def display_ball_details(self, color):
        if color == "Red":
            print(self.red_balls_container)
        elif color == "Green":
            print(self.green_balls_container)
        elif color == "Blue":
            print(self.blue_balls_container)
        elif color == "Yellow":
            print(self.yellow_balls_container)


# Use different values to test your program
ball1 = Ball("Red", "A")
ball2 = Ball("Blue", "B")
ball3 = Ball("Yellow", "B")
ball4 = Ball("Blue", "A")
ball5 = Ball("Yellow", "A")
ball6 = Ball("Green", "B")
ball7 = Ball("Green", "A")
ball8 = Ball("Red", "B")
ball_list = Stack(8)
ball_list.push(ball1)
ball_list.push(ball2)
ball_list.push(ball3)
ball_list.push(ball4)
ball_list.push(ball5)
ball_list.push(ball6)
ball_list.push(ball7)
ball_list.push(ball8)

# Create objects of Game class, invoke the methods and test the program
game = Game(ball_list)
game.grouping_based_on_color()
game.display_ball_details("Red")
game.display_ball_details("Green")
game.display_ball_details("Blue")
game.display_ball_details("Yellow")
game.rearrange_balls("Red")
game.rearrange_balls("Green")
game.rearrange_balls("Blue")
game.rearrange_balls("Yellow")
game.display_ball_details("Red")
game.display_ball_details("Green")
game.display_ball_details("Blue")
game.display_ball_details("Yellow")
