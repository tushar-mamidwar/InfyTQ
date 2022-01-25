'''
Problem Statement
Write a function to find and return the index of the minimum element in a sub-list. Follow the instructions provided in template code.

Test your code by passing different values for num_list and start_index.

You can reuse this function to find the next minimum element in the list during each pass while implementing the selection sort algorithm.
'''
# lex_auth_0127667370895278083332


def find_next_min(num_list, start_index):
    # Remove pass and write the logic to find the minimum element in a sub-list and return the index of the identified element in the num_list.
    # start_index indicates the start index of the sub-list
    minimum = num_list[start_index]
    minimum_index = start_index
    for i in range(start_index, len(num_list)):
        if num_list[i] < minimum:
            minimum = num_list[i]
            minimum_index = i
    return minimum_index


# Pass different values to the function and test your program
num_list = [10, 2, 100, 67]
start_index = 1
print("Index of the next minimum element is",
      find_next_min(num_list, start_index))
