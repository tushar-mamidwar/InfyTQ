"""
Problem Statement

Write a python function, create_largest_number(), which accepts a list of numbers
and returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.


Sample Input            Expected Output

23,1,445                   553423
"""

#lex_auth_01269441913243238467-

def create_largest_number(number_list):
    number_list.sort()
    number_list=number_list[::-1]
    largest_number=""
    for i in number_list:
        largest_number+=str(i)
    return int(largest_number)
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)