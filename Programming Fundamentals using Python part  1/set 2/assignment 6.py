"""
Problem Statement
Write a python program to solve a classic ancient Chinese puzzle.

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Sample Input            Expected Output

heads-150 legs-400          100 50

heads-3 legs-11           No solution

heads-3 legs-12             0 3

heads-5 legs-10             5 0
"""
#lex_auth_012693810762121216155

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=heads
    rabbit_count=0
    while not (chicken_count*2+rabbit_count*4==legs) and chicken_count!=0:
        chicken_count-=1
        rabbit_count+=1

    if chicken_count*2+rabbit_count*4 == legs:
        print(chicken_count, rabbit_count)
    else:
        print(error_msg)

    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count



    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your progra
solve(38,131)
