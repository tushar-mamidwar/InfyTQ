'''
Problem Statement
Implement the merge sort algorithm to sort a list of numbers in ascending order.
'''
# lex_auth_0127667368801157123532


def merge_sort(num_list):
    # Remove pass and write the logic here to return the sorted list
    if len(num_list) == 1:
        return num_list
    left_list = num_list[:len(num_list)//2]
    right_list = num_list[len(num_list)//2:]
    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)
    merged_list = merge(sorted_left_list, sorted_right_list)
    return merged_list


def merge(left_list, right_list):
    # Remove pass and write the logic to merge the elements in the left_list and right_list and return the sorted list
    i = 0
    j = 0
    merged_list = []
    len_left_list = len(left_list)
    len_right_list = len(right_list)
    while i < len_left_list and j < len_right_list:
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1
    while i < len_left_list:
        merged_list.append(left_list[i])
        i += 1
    while j < len_right_list:
        merged_list.append(right_list[j])
        j += 1
    return merged_list


num_list = [34, 67, 8, 19, 2, 23, 1, 91]
print("Before sorting:", num_list)
sorted_list = merge_sort(num_list)
print("After sorting:", sorted_list)
