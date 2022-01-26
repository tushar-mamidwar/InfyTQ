"""
Problem Statement
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.

Write a python function which performs the run length encoding for a given String and returns the run length encoded String.

Provide different String values and test your program

Sample Input                    Expected Output

AAAABBBBCCCCCCCC                    4A4B8C

AABCCA                              2A1B2C1A
"""

# lex_auth_012693816331657216161


def encode(message):
    count = 1
    message += " "
    encoded_message = ""
    for i in range(0, len(message) - 1):
        if message[i] == message[i + 1]:
            count += 1
        else:
            encoded_message += str(count) + message[i]
            count = 1
    return encoded_message

    # Remove pass and write your logic here


# Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
