#lex_auth_01269442963365068878

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor
    if(is_prime(list_of_factors[-1],list_of_factors[-1]//2)):
        return list_of_factors[-1]
    else:
        return find_largest_prime_factor(list_of_factors[:-1])

def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    factors=find_factors(num)
    return find_largest_prime_factor(factors)

def find_g(num,sum=0,count=0):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    if count<9:
        return find_g(num + 1, sum + find_f(num), count + 1)
    else:
        return sum

#Note: Invoke function(s) from other function(s), wherever applicable.
print(find_g(10))
