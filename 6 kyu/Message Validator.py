def is_a_valid_message(message):
    count = ""
    num = 0
    for c in message:            
        if ord(c) >= ord('0') and ord(c) <= ord('9'):
            count = count + c
        elif count != "":
            num = int(count)
            count = ""
            num -= 1
        else:
            if num < 0:
                return False
            else:
                num -= 1
    if num > 0 or count != "":
        return False
    return True
    pass
