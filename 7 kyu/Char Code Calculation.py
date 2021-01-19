def calc(x):
    total1 = ""
    n = 0
    
    for c in x:
        total1 += str(ord(c))
    
    for c in total1:
        if c == '7':
            n += 6
    
    return n
