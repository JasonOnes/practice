"""bubble sort"""

def sort_list(num_list):
    #changes = 0
    for num in num_list:
        for idx in range(len(num_list)-1):
            if num_list[idx] > num_list[idx+1]:
                num_list[idx], num_list[idx+1] = num_list[idx+1], num_list[idx]

                #changes += 1
    #while changes > 0:
    #    sort_list(num_list)
    print(num_list)

sort_list([1000000, 1, 11, 5,100, -9, 31, 9, 99, 65, 2])
