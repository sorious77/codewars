def solution(s):
    answer = ""
    for c in s:
        if c.isupper() == True:
            answer += " " + c
        else:
            answer += c
    return answer
