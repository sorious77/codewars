def sum_of_minimums(numbers):
    sum = 0
    
    for i in numbers:
        min = i[0]
        for j in i:
            if min > j:
                min = j
        sum += min
    
    return sum
    pass
