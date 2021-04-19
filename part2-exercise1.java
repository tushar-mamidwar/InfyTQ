#lex_auth_01269437118923571233

def factorial(number):
    fact=1
    if number==0:
        return 1
    for i in range(2,number+1):
        fact*=i
    return fact
        


def find_strong_numbers(num_list):
    strong_list=[]
    for i in num_list:
        result=0
        for j in str(i):
            result+=factorial(int(j))
        if result==i:
            strong_list.append(i)
    return strong_list
            


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
