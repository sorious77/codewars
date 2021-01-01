def time_convert(num):
    if num <= 0:
        return "00:00"
    return "%02d:%02d" %(num/60,num%60)
