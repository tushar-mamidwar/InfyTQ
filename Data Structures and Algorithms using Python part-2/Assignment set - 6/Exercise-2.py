"""
Problem Statement
The Rotary club has planned to organize several events on the Women’s day. The volunteers are given a 
list of activities and the starting time and ending time of those activities.

Write a python function which accepts the activity list, start_time list and finish_time list. The function 
should find out and return the list of maximum number of activities that can be performed by a 
single person.

Assume that a person can work only on a single activity at a time. If an activity performed by a person ends at x unit time then he/she can take up the next activity which is starting at any time greater than or equal to x+1.

Refer table below for sample input and expected output:

Sample Input                                        Expected Output

activity_list - [1, 2, 3, 4, 5, 6]
start_time_list = [1, 3, 0, 5, 8, 5]                  [1, 2, 4, 5]
finish_time_list = [2, 4, 6, 7, 9, 9]

activity_list - [1, 2, 3, 4, 5, 6]
start_time_list = [5, 4, 8, 2, 3, 1]                     [6, 1]
finish_time_list = [13, 6, 16, 7, 5, 4]
"""
# lex_auth_0127667392950599683407
def find_maximum_activities(activity_list, start_time_list, finish_time_list):
    # Remove pass and write your logic here
    for i in range(len(activity_list)):
        min_index = find_next_min(finish_time_list, i)
        swap(activity_list, i, min_index)
        swap(start_time_list, i, min_index)
        swap(finish_time_list, i, min_index)
    start_time = start_time_list[0]
    finish_time = finish_time_list[0]
    output_list = [activity_list[0]]
    for i in range(len(activity_list)):

        if start_time_list[i] > finish_time:
            finish_time = finish_time_list[i]
            output_list.append(activity_list[i])
    return output_list


def swap(num_list, first_index, second_index):
    # Remove pass and copy the code written earlier for this function
    temp = num_list[first_index]
    num_list[first_index] = num_list[second_index]
    num_list[second_index] = temp


def find_next_min(num_list, start_index):
    # Remove pass and copy the code written earlier for this function
    min = num_list[start_index]
    min_index = start_index
    for i in range(start_index + 1, len(num_list)):
        if num_list[i] < min:
            min = num_list[i]
            min_index = i
    return min_index


def selection_sort(num_list):
    # Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    pass


# Pass different values to the function and test your program
activity_list = [1, 2, 3, 4, 5, 6]
start_time_list = [1, 3, 0, 5, 8, 5]
finish_time_list = [6, 4, 2, 9, 9, 2]
print("Activities:", activity_list)
print("Start time of the activities:", start_time_list)
print("Finishing time of the activities:", finish_time_list)

result = find_maximum_activities(activity_list, start_time_list, finish_time_list)
print("The maximum set of activities that can be completed:", result)
print(finish_time_list)
