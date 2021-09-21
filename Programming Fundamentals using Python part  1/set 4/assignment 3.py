"""
problem statement

Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below.
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.

The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.

and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number
of WRONG answers.
Assume that the words contain only uppercase letters and the maximum word length is 10.

Sample Input

Expected Output

{"THEIR": "THEIR", "BUSINESS": "BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}

[2, 2, 1]

"""


# lex_auth_01269444890062848087

def find_correct(word_dict):
    output_list=[0,0,0]
    for correct_spelling,contestant_spelling in word_dict.items():
        count=0
        if len(correct_spelling)!=len(contestant_spelling):
            output_list[2]+=1
            continue
        for i in range(len(correct_spelling)):
            if correct_spelling[i]!=contestant_spelling[i]:
                count+=1

        if count==0:
            output_list[0]+=1
        elif count<=2:
            output_list[1]+=1
        else:
            output_list[2]+=1

    return output_list


word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS", "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))