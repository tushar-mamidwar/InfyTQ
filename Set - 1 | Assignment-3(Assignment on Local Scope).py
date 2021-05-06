#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    cost_of_fuel_perkm=70/10
    profit=no_of_passengers*80- distance * cost_of_fuel_perkm
    if profit<0:
        return -1
    return profit



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
