def index(array, n):
    if len(array) - 1 < n:
        return -1
    return array[n] ** n
