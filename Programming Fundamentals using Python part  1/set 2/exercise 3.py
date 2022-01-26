"""
Problem Statement


Write a python program that displays a message as follows for a given number:

1.If it is a multiple of three, display "Zip"
2.If it is a multiple of five, display "Zap".
3.If it is a multiple of both three and five, display "Zoom".
4.If it does not satisfy any of the above given conditions, display "Invalid".
"""
# lex_auth_01269363490743091290


def display(num):
    message = ""
    # write your logic here
    if not num % 3 and not num % 5:
        message = "Zoom"
    elif not num % 3:
        message = "Zip"
    elif not num % 5:
        message = "Zap"
    else:
        message = "Invalid"
    return message


# Provide different values for num and test your progra
message = display(15)
print(message)
