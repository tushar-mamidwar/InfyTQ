"""
Problem Statement

Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number
where

Consider AI as the value for airline
src and dest should be the first three characters of the source and destination cities.
number should be auto-generated starting from 101
The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.

Sample Input                                        Expected Output

airline = AI
source = Bangalore                        ['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108',
destination = London                        'AI:Ban:Lon:109', 'AI:Ban:Lon:110']
no_of_passengers = 10

airline = BA
source = Australia                       ['BA:Aus:Fra:101', 'BA:Aus:Fra:102']
destination = France
no_of_passengers = 2
"""


# lex_auth_012693763253788672132

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    # Write your logic here
    count = 100
    for i in range(0, no_of_passengers):
        count += 1
        ticket_number_list.append(airline + ":" + source[:3] + ":" + destination[:3] + ":" + str(count))
        if (len(ticket_number_list)) > 5:
            ticket_number_list.pop(0)
    # Use the below return statement wherever applicable
    return ticket_number_list


# Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI", "Bangalore", "London", 7))
