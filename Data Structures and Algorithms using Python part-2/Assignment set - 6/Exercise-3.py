# lex_auth_0127667323215544323487


def max_sum_is(num_list):
    # Remove pass and write your logic here
    msis = []
    length = len(num_list)
    for num in num_list:
        msis.append(num)

    for i in range(length):
        for j in range(i):
            if num_list[i] > num_list[j] and msis[i] < msis[j] + num_list[i]:
                msis[i] = msis[j] + num_list[i]
    print(i, j)
    return max(msis)


# Pass different values to the function and test your program
num_list = [1, 101, 2, 3, 100, 4, 5]
print("Sum of the maximum sum increasing subsequence is :", max_sum_is(num_list))
