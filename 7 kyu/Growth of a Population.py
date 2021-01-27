def nb_year(p0, percent, aug, p):
    ans = 0
    while p0 < p:
        print(p0)
        p0 = p0 + int(p0 * (0.01 * percent)) + aug
        ans += 1
    print(p0)
    return ans
