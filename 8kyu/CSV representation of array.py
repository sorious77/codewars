def toCsvText(array) :
    result = ''
    iCount = 0
    for i in array:
        jCount = 0
        iCount += 1
        for j in i:
            result += str(j)
            jCount += 1
            if jCount < len(i):
                result += ','
        if iCount < len(array):
            result += '\n'
    return result
