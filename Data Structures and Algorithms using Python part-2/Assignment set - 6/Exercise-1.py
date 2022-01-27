"""
Use Greedy approach and implement the solution for solving the change making problem.
"""
# lex_auth_0127667342200995843410


def make_change(denomination_list, amount):
    """Remove pass and implement the Greedy approach to make the change for the amount using the currencies in the denomination list.
    The function should return the total number of notes needed to make the change. If change cannot be obtained for the given amount, then return -1. Return 1 if the amount is equal to one of the currencies available in the denomination list."""
    count = 0
    i = 0
    denomination_list.sort(reverse=True)
    while amount != 0:
        if denomination_list[i] <= amount:
            amount = amount - denomination_list[i]
            count += 1
        else:
            if i < len(denomination_list) - 1:
                i += 1
            else:
                break

    if amount == 0:
        return count
    else:
        return -1


# Pass different values to the function and test your program
amount = 20
denomination_list = [1, 15, 10]
print(make_change(denomination_list, amount))
