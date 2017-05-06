def sum_evens(num_list):
    total = 0
    for num in num_list:
        if num % 2 == 0:
            total += num
        else:
            total += 0
    return total
