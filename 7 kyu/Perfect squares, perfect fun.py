def square_it(digits):
    s = str(digits)
    length = len(s) ** 0.5
    answer = ""
    
    print(length)
    
    if int(length) - length == 0:
        count = 0
        for c in s:
            count += 1
            answer += c
            
            if count % length == 0 and count != len(s):
                answer += '\n'
            
    else:
        return "Not a perfect square!"
    
    return answer
    # Your code here
