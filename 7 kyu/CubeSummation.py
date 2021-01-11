def cube_sum(n, m):
    if n > m:
        temp = n
        n = m
        m = temp
    sum = 0
    for i in range(n+1, m+1):
        sum += i ** 3
    return sum
