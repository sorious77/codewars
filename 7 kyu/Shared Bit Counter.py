def shared_bits(a, b):
    if str(bin(a&b)).count('1') >= 2 :
        return True
    return False
