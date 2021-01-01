def filter_long_words(sentence, n):
    a = []
    str = sentence.split()
    for s in str:
        if len(s) > n :
            a.append(s)
    return a
    pass
