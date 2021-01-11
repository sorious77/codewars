def get_even_numbers(arr):
    answer = []
    for i in arr:
        if i % 2 == 0:
            answer.append(i)
    return answer
