'''
Problem Statement
Now we know that comparison and swapping are two basic operations required for sorting, let’s write a function to swap two numbers in a list.

Complete the given function by following the instructions provided in template code. Test your code by passing different values for num_list, first_index and second_index.
'''
# lex_auth_0127667345256611843470


def swap(num_list, first_index, second_index):
    # Remove pass and write your logic here
    # As python lists are mutable, num_list need not be returned after swapping
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


# Pass different values to the function and test your program
num_list = [2, 3, 89, 45, 67]
print("List before swapping:", num_list)
swap(num_list, 1, 2)
print("List after swapping:", num_list)
