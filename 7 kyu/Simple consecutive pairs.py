def pairs(ar):
    answer = 0
    i = 0
    
    while i < len(ar):
        if i + 1 >= len(ar):
            break
        
        if abs(ar[i] - ar[i+1]) == 1:
            answer += 1
        
        i += 2
        
    return answer
