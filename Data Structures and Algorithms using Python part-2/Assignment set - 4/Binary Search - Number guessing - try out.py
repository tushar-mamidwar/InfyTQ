# DSA-Tryout
import random


def find_it(num, element_list):
    # Remove pass and write the logic to search num in element_list using binary search algorithm
    # Return the total number of guesses made
    low = 0
    high = len(element_list) - 1
    no_of_guesses = 0
    while low <= high:
        mid = (low + high) // 2
        no_of_guesses += 1
        if element_list[mid] == num:
            return no_of_guesses
        elif num < element_list[mid]:
            high = mid - 1
        else:
            low = mid + 1


# Initializes a list with values 1 to n in ascending order and returns it


def initialize_list_of_elements(n):
    list_of_elements = []
    for i in range(1, n + 1):
        list_of_elements.append(i)
    return list_of_elements


def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    list_of_elements = initialize_list_of_elements(n)
    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    random_number = random.randrange(1, n + 1)
    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    no_of_guesses = find_it(random_number, list_of_elements)
    print(list_of_elements)
    print(random_number)

    print(no_of_guesses)


# Pass different values to play() and observe the output
play(10)
