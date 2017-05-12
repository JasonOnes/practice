def sum_of_initial_odds(nums):
    """Returns the sum of all the initial odd numbers until an even number 
       occurs."""
    total = 0
    for num in nums:
        if num % 2 == 0:
            return total
        else:
            total += num
    return total
