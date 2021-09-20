"""
Problem Statement

Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences

Sample Input                                Expected Output

[1,1,5,100,-20,-20,6,0,0]                           3

[10,20,30,40,30,20]                                 0

[1,2,2,3,4,4,4,10]                                  3

"""


# lex_auth_012693750719488000124

def get_count(num_list):
    count = 0
    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            count += 1

    # Write your logic here

    return count


# provide different values in list and test your program
num_list = [1, 1, 1, 5, 100, -20, -20, 6, 0, 0]
print(get_count(num_list))
