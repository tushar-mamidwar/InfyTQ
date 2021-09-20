"""
Problem Statement

Write a Python program to find the sum of digits of a given number. E.g. Sum of number 123 will be 6
Note: Initialize the number with various values and test your program.
"""

def find_sum_of_digits(number):
    sum_of_digits=0
    #Write your logic here
    for digit in str(number):
        sum_of_digits+=int(digit)
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)