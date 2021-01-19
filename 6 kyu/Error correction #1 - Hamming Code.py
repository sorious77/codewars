def encode(string):
    bits = ""
    for c in string:
        binStr = bin(ord(c))[2:]
        for ch in f'{binStr:0>8}':
            bits += ch + ch + ch        
    return bits

def decode(bits):
    string = ""
    start = 0
    end = 3
    temp = ""
    
    while end <= len(bits):
        curStr = bits[start:end]
        countOne = 0
        countZero = 0
        for c in curStr:
            if c == '0':
                countZero += 1
            else:
                countOne += 1
        if countOne > countZero:
            temp += "1"
        else:
            temp += "0"
        
        if len(temp) == 8:
            string += chr(int(temp, 2))
            temp = ""
        
        start = end
        end += 3
        
            
    return string
