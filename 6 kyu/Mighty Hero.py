def count_of_heads(initial, n, swings):
    for i in range(1, swings + 1):
        temp = n
        for j in range(1, i + 1):
            temp *= j
        initial = initial - 1 + temp
        
    return initial
