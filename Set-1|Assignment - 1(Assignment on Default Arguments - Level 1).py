#lex_auth_0127382164803993601239

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    if filter_func:
        list_of_num=filter_func
    sum=0
    for num in list_of_num:
        sum+=num
    return sum
        
    
    

def even(data):
    even=[]
    for i in data:
        if not i%2:
            even.append(i)
    return even
def odd(data):
    odd=[]
    for i in data:
        if i%2:
            odd.append(i)
    return odd

sample_data = range(1,11)

print(sum_of_numbers([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],even([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])))
