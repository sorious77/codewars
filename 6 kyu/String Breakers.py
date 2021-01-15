def string_breakers(n, st):
    count = 0
    answer = ""
    for c in st:
        if c == ' ':
            continue
        if count == n:
            count = 0
            answer += "\n"
        answer += c
        count += 1
    return answer
