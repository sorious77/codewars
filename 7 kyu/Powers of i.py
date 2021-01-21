def pofi(n):
    if n % 4 == 0:
        return '1'
    elif n % 4 == 1:
        return 'i'
    elif n % 4 == 2:
        return '-1'
    return '-i'
