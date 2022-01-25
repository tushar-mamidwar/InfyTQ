'''
Problem Statement
Let’s compare selection sort and bubble sort algorithms in this exercise.

Combine the selection sort and bubble sort programs as per the template code provided below and display the number of passes for each of them.

Invoke both the functions (selection_sort() and bubble_sort()) using the following two lists and observe the results.

Case 1: [8,2,19,34,23, 67, 91]

Case 2: [91,8,19,23,34,67,2]
'''

# lex_auth_0127667385791856643328


def swap(num_list, first_index, second_index):
    # Remove pass and copy the code earlier written for this function
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def find_next_min(num_list, start_index):
    # Remove pass and copy the code earlier written for this function
    min = num_list[start_index]
    min_index = start_index
    for i in range(start_index+1, len(num_list)):
        if min > num_list[i]:
            min = num_list[i]
            min_index = i

    return min_index


def selection_sort(num_list):
    # Remove pass and copy the code earlier written for this function
    # Modify it to return the total number of passes the algorithm has gone through to sort the list
    total_no_of_passes = 0
    for i in range(len(num_list)-1):
        total_no_of_passes += 1
        min_index = find_next_min(num_list, i)
        if i != min_index:
            swap(num_list, i, min_index)
    return total_no_of_passes


def bubble_sort(num_list):
    total_no_of_passes = 0
    end_index = len(num_list)
    for i in range(end_index-1):
        total_no_of_passes += 1
        swapped = False
        for j in range(end_index-i-1):
            if num_list[j] > num_list[j+1]:
                swap(num_list, j, j+1)
                swapped = True
        if swapped == False:
            break
    return total_no_of_passes


num_list = [8, 2, 19, 34, 23, 67, 91]
num_list = [91, 8, 19, 23, 34, 67, 2]
print("Selection Sort - No. of passes:", selection_sort(num_list))
print(num_list)
num_list = [8, 2, 19, 34, 23, 67, 91]
num_list = [91, 8, 19, 23, 34, 67, 2]
print("Bubble Sort - No. of passes:", bubble_sort(num_list))
print(num_list)
