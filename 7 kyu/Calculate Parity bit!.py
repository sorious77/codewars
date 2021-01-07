def check_parity(parity, bin_str): 
    if bin_str.count("1") % 2 == 0 :
        if parity == 'even':
            return 0
        else:
            return 1
    else:
        if parity == 'even':
            return 1
        else:
            return 0
    pass
