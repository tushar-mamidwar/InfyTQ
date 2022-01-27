def fibonacci(num):
    global count
    count += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        if num in memo:
            return memo[num]
        else:
            memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
            return memo[num]


count = 0
memo = {}
print(fibonacci(50))
print(count)
