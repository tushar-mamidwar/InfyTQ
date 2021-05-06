#lex_auth_01269441810970214471

def check_double(number):
    double=number*2
    for i in str(number):
        if i in str(double):
            continue
        else:
            return False
    return True

#Provide different values for number and test your program
print(check_double(125874))
