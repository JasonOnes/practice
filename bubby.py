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

def sort_list2(num_list):
    max_num = 0
    new_list = []
    for num in num_list:
        if num > max_num:
            max_num = num
            x = num_list.index(max_num)
            #new_list.append(num_list.pop(num_list[x]))

            print(x)
    print(new_list)

sort_list2([2, 66, 9823, 9, 1])
