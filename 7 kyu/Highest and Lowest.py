def high_and_low(numbers):
    numbers = numbers.split()
    max = int(numbers[0])
    min = int(numbers[0])
    
    for i in numbers:
        if max < int(i):
            max = int(i)
        if min > int(i):
           min = int(i)
    
    numbers = f'{max} {min}'
    
    return numbers
