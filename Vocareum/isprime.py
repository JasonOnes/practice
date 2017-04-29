def is_prime(n):
    if n == 2 or n == 3:
        print('t')
        return True
    else:
        for x in range(2, n):
            for y in range(2, n):
                if x * y == n:
                    print("f")
                    return False

    print("t")
    return True

is_prime(2227)
