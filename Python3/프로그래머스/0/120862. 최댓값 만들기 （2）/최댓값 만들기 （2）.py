def solution(numbers):
    answer = 0
    max = -float('inf')
    for i in range (len(numbers)): 
        number1 = numbers[i]
        for j in range(i + 1, len(numbers)): # 이래야 중복 안되게 곱한다. 
            number2 = numbers[j]
            if number1 * number2 > max:
                max = number1 * number2
           
    return max