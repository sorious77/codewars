def equalize(arr):
    answer = []
    
    for i in arr:
        s = ""
        if i >= arr[0]:
            s = "+"
        else:
            s = "-"
        s += str(abs(arr[0] - i))
        answer.append(s)
    
    return answer
