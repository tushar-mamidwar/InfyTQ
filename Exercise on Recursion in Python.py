#lex_auth_01269437527007232044

def human_pyramid(no_of_people):
    if no_of_people==1:
        return 50
    else:
        return 50*no_of_people+human_pyramid(no_of_people-2)

def find_maximum_people(max_weight):
    no_of_people=1
    while(human_pyramid(no_of_people)<=max_weight):
        no_of_people+=2
    return no_of_people-2

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)
