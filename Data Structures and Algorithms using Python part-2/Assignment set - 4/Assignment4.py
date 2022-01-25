'''
Problem Statement
Given a list of numbers sorted in ascending order. Write a python function which searches for a given number in the list. The given number may occur more than once in the list. The function should return the index position at which the last occurrence of the given element is found. If the number is not found, return -1.
'''
# lex_auth_0127667364335943683412


def last_instance(num_list,  start,  end,  key):
    # Remove pass and write your logic here
    low = start
    high = end
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if num_list[mid] == key:
            break
        elif num_list[mid] > key:
            high = mid-1
        elif num_list[mid] < key:
            low = mid+1
    else:
        return -1
    i = mid
    while i < end:
        if num_list[i+1] == key:
            i += 1
        else:
            break
    return i


num_list = [2, 3, 4, 4, 5, 6, 7]
start = 0
end = len(num_list)-1
key = 4  # Number to be searched
# Pass different values for num_list, start,end and key and test your program
result = last_instance(num_list, start, end, key)

if(result != -1):
    print("The index position of the last occurrence of the number:", result)
else:
    print("Number not found")
