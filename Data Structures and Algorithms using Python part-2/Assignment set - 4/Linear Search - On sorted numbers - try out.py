# DSA-Tryout

import random


def find_it(num, element_list):
    # Remove pass and write the logic to search num in element_list using linear search algorithm
    # Return the total number of guesses made
    no_of_guesses = 0
    for number in element_list:
        no_of_guesses += 1
        if number == num:
            return no_of_guesses
            break


# Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    asc_list_of_elements = []
    for i in range(1, n+1):
        asc_list_of_elements.append(i)
    desc_list_of_elements = []
    for j in range(n, 0, -1):
        desc_list_of_elements.append(j)
    return asc_list_of_elements, desc_list_of_elements


def play(n):
    # Step 1: Invoke initialize_list_of_elements() by passing n
    asc_list_of_elements, desc_list_of_elements = initialize_list_of_elements(
        n)

    # Step 2: Generate a random number from the list of elements. The number should be between 1 and n (both inclusive)
    random_number = random.randrange(1, n+1)

    # Step 3: Invoke find_it() by passing the number generated at Step 2 and list generated at Step 1 and display the return value
    asc_no_of_guesses, desc_no_of_guesses = find_it(
        random_number, asc_list_of_elements), find_it(random_number, desc_list_of_elements)

    print('ascending list:', asc_list_of_elements)
    print('descending list:', desc_list_of_elements)
    print(random_number)
    print('no_of_guesses for asc:', asc_no_of_guesses)
    print('no_of_guesses for desc:', desc_no_of_guesses)
    # Remove pass and write the code to implement the above three steps.


# Pass different values to play() and observe the output
play(10)
