def mxdiflg(a1, a2):
    a1.sort(key=len)
    a2.sort(key=len, reverse=True)
    
    print(a1[0])
    print(a2[0])
    
    return abs(len(a1[0]) - len(a2[0]))
