def find_uniq(arr):
    arr_set = set(arr)
    n = 0
    
    for i in arr_set:
        if arr.count(i) == 1:
            n = i
    return n
