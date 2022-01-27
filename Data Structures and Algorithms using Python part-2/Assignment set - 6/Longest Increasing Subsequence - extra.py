list1 = [2, 2, 2, 3, 9, 6, 1, 5, 10]
i = 1
j = 0
increasing_subsequence = [1] * len(list1)
for i in range(1, len(list1)):
    for j in range(i):
        if list1[j] < list1[i]:
            if increasing_subsequence[j] >= increasing_subsequence[i]:
                increasing_subsequence[i] = increasing_subsequence[j] + 1
print(max(increasing_subsequence))
print("Longest Increasing Subsequence is:")
j = 0
longest_inc_subseq = []
for i in range(len(list1)):
    if increasing_subsequence[i] == j + 1:
        longest_inc_subseq.append(list1[i])
        j += 1
print(longest_inc_subseq)
