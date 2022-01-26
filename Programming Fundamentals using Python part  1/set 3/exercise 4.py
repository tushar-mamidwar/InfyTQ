"""
Problem Statement


Debug the given program so as to get the output as shown:

Passenger 1 : Proceed for baggage check.

Passenger 2 : Proceed for baggage check.

Passenger 3 : Maximum baggage weight allowed is 30kg.

Passenger 4 : Maximum baggage weight allowed is 30kg.

Passenger 5 : Proceed for baggage check.

No. of passengers who cleared baggage check: 3
"""

# lex_auth_01273338869591244855
count = 0
i = 1
for baggage_weight in 29, 30, 31, 32, 28:
    if (baggage_weight >= 1 and baggage_weight <= 30):
        print("Passenger", i, ": Proceed for baggage check.")
        count += 1
    else:
        print("Passenger", i, ": Maximum baggage weight allowed is 30kg.")
    i += 1

print("No. of passengers who cleared baggage check:", count)

