def solve(a,b):
    answer = []
    for s in b:
        count = 0
        for sA in a:
            if s == sA:
                count += 1
        answer.append(count)
    return answer
