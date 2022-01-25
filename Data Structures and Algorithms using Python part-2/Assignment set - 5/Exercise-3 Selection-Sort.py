'''
Using the swap() and find_next_min() functions, implement the selection sort algorithm to sort a list of numbers in ascending order.
'''
# lex_auth_0127667356693872643343


def swap(num_list, first_index, second_index):
    # Remove pass and copy the code written earlier for this function
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def find_next_min(num_list, start_index):
    # Remove pass and copy the code written earlier for this function
    min = num_list[start_index]
    min_index = start_index
    for i in range(start_index+1, len(num_list)):
        if num_list[i] < min:
            min = num_list[i]
            min_index = i
    return min_index


def selection_sort(num_list):
    # Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    for i in range(len(num_list)):
        min_index = find_next_min(num_list, i)
        swap(num_list, i, min_index)


# Pass different values to the function and test your program
num_list = [8, 2, 19, 34, 23, 67, 91]
print("Before sorting;", num_list)
selection_sort(num_list)
print("After sorting:", num_list)
