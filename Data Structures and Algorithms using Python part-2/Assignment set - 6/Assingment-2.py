# lex_auth_0127667363417702403454
# ----Selection Sort-----
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


def selection_sort(num_list, num_list2):
    # Remove pass and implement the selection sort algorithm to sort the elements of num_list in ascending order
    for i in range(len(num_list)):
        min_index = find_next_min(num_list, i)
        swap(num_list, i, min_index)
        swap(num_list2, i, min_index)


def find_number_of_platforms(arrival_time_list, departure_time_list):
    # Remove pass and test your program
    selection_sort(arrival_time_list, departure_time_list)
    train_on_station = [departure_time_list[0]]
    max_no_of_platform = 1
    len_train_on_station = 1
    for i in range(1, len(arrival_time_list)):
        for j in range(len(train_on_station)):
            if arrival_time_list[i] >= train_on_station[j]:
                train_on_station.pop(j)
                len_train_on_station -= 1
                break
        else:
            len_train_on_station += 1
            train_on_station.append(departure_time_list[i])
        if len_train_on_station > max_no_of_platform:
            max_no_of_platform = len_train_on_station
    return max_no_of_platform


# Pass different values to the function and test your program
arrival_time_list = [800, 810, 900, 740, 1200, 1400]
departure_time_list = [2300, 2000, 1200, 1349, 1500, 2120]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:", departure_time_list)
print(
    "Minimum number of platforms required :",
    find_number_of_platforms(arrival_time_list, departure_time_list),
)
