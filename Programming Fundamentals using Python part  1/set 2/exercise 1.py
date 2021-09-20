"""
Problem Statement
The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
Rate per Adult: Rs. 37550.0
Rate per Child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers)
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.

Test the program with different input values for number of adults and children.

            Sample Input                                            Expected Output
Number of adults    Number of children

        5                   2                                   Total Ticket Cost: 204910.35

        3                   1                                   Total Ticket Cost: 120535.5

"""

#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    total_ticket_cost=((no_of_adults*37550+no_of_children*37550/3)*1.07)*0.9

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your progra
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
