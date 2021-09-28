"""
Problem Statement
Animal Welfare Trust is on a visit to the circus camp to have a look at the four talking parrots added to the camp.
A parrot is identified by its name and color. Apart from this, the trust has asked to assign a unique number
for each parrot. The unique number should begin with 7001 and should be auto-incremented by 1 for every new
parrot added to the camp.

Identify the class name and attributes so as to represent parrots from the list given.
- beak_color
- __init__(name,color)
- name
- Parrot
- counter->static
- color
- Parrots
- unique_number

Write a Python program to implement the class chosen with its attributes and methods. Represent few parrots,
display their names, color and unique number.

Note: Consider all the attributes to be private and methods to be public. Include getter methods for all the
instance variables.
"""


class Parrot:
    __counter = 7000

    def __init__(self, name, color):
        Parrot.__counter += 1
        self.__name = name
        self.__color = color
        self.__unique_number = Parrot.__counter

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_unique_number(self):
        return self.__unique_number


parrot1 = Parrot("parrot1", "Green")
parrot2 = Parrot("parrot2", "Red")
print(parrot1.get_name(), parrot1.get_color(), parrot1.get_unique_number())
print(parrot2.get_name(), parrot2.get_color(), parrot2.get_unique_number())
