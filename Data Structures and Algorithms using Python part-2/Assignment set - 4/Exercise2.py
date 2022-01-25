'''
Problem Statement
Write a python function which searches for a particular substring in a given string. The substring may occur more than once in the string. If found, return the number of occurrences of the substring in the string. Otherwise, return 0.

Perform case sensitive string comparison wherever necessary.
'''
# lex_auth_0127667355651112963444


def pattern_search(text, pattern):
    # Remove pass and write your logic here
    i = 0
    occurrences = 0
    while i < len(text):
        if text[i] == pattern[0]:
            for character in pattern:
                if text[i] != character:
                    break
                else:
                    i += 1
            else:
                occurrences += 1
        i += 1
    return occurrences


# Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result = pattern_search(text, pattern)
print("The given text:", text)
print("Pattern:", pattern)
print("No. of occurrences of the pattern :", result)
