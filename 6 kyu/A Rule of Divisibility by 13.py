def thirt(n):
    if n < 100:
        return n
    
    print(n)
    
    thirt_arr = [1,10,9,12,3,4]
    s = str(n)
    sum = 0
    index = 0
    
    for i in s[::-1]:
        sum += int(i) * thirt_arr[index]
        index = (index + 1) % 6
        
    return thirt(sum)
