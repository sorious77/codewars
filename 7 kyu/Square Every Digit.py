def square_digits(num):
    s = str(num)
    answer = ''
    for ch in s:
        answer += str(int(ch) ** 2)
    return int(answer)
    pass
