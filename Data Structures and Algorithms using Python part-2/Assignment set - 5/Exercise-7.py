# lex_auth_0127667363860725763513
def swap(num_list, index1, index2):
    temp = num_list[index1]
    num_list[index1] = num_list[index2]
    num_list[index2] = temp


def arrange_tickets(tickets_list):
    high = len(tickets_list)-1
    for i in range(high):
        swapped = False
        for j in range(high-i):
            if int(tickets_list[j][1:]) > int(tickets_list[j+1][1:]):
                swap(tickets_list, j, j+1)
                swapped = True
        if swapped == False:
            break
    j = 0
    while j < len(tickets_list):
        if int(tickets_list[j][1:]) > 10:
            break
        j += 1
    i = 0
    while i < 10:
        if int(tickets_list[i][1:]) != i+1:
            tickets_list.insert(i, tickets_list[j])
            j += 2
        i += 1
    return tickets_list[:10]


tickets_list = ['T5', 'T7', 'T1', 'T2', 'T8',
                'T15', 'T17', 'T19', 'T6', 'T12', 'T13']
print("Ticket ids of all the available students :")
print(tickets_list)
result = arrange_tickets(tickets_list)
print()
print("Ticket ids of the ten students in Group-1:")
print(result)
