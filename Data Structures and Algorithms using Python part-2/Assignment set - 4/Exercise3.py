'''
Problem Statement
Write a python function which accepts a list of numbers, the start index and the end index. The numbers are arranged in the list in increasing order until a particular index and after that it is arranged in decreasing order.

This function should find and return the index position at which the increasing list starts decreasing.

Sample Input                        Expected Output

[1,4,7,8,9,5,4], 0, 6                       5
'''
# lex_auth_0127667385795952643524


def find_decreasing_start(list1, start, end):
    # Remove pass and write your logic here
    for i in range(start+1, end+1):
        if list1[i] < list1[i-1]:
            return i


# Use different values for list1 and test your program
list1 = [1, 4, 7, 8, 9, 5, 4]
start = 0
end = len(list1)-1
result = find_decreasing_start(list1, start, end)
print("The index position at which the increasing array starts decreasing is:", result)
