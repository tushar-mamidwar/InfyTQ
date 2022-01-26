"""
The school has reopened after the holidays. Maria, the faculty, wants to arrange her students in the increasing order of their heights.

Write a python function which accepts a list of student names and a list of their heights. Assume there is one-to-one correspondence between the two lists. Arrange the students in the increasing order of their height and return a list containing the list of students and their heights.
"""


def swap(num_list, index1, index2):
    temp = num_list[index1]
    num_list[index1] = num_list[index2]
    num_list[index2] = temp


def find_next_min(num_list, start_index):
    min = num_list[start_index]
    min_index = start_index
    for i in range(start_index + 1, len(num_list)):
        if num_list[i] < min:
            min = num_list[i]
            min_index = i
    return min_index


# lex_auth_0127667319794565123439


def order_heights(student_list, height_list):
    # Write your logic here
    for i in range(len(height_list)):
        min_index = find_next_min(height_list, i)
        swap(height_list, i, min_index)
        swap(student_list, i, min_index)
    return [student_list, height_list]


# Pass different values to the function and test your program
student_list = ["Santa", "Tris", "Arun", "Rachel", "John"]
height_list = [132.7, 129.2, 135, 130.6, 140]
print("Initial student details :")
print("The students:", student_list)
print("Their heights:", height_list)
print()
result = order_heights(student_list, height_list)
print("After arranging the students in the order of their height:")
print("The students :", result[0])
print("Their heights:", result[1])
