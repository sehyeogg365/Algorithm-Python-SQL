def solution(numbers):
    answer = 0
    max = 0
    
    for num in numbers:
        if num > max:
            max = num
            
     # 최대값을 numbers배열에서 제거한다
    numbers.remove(max)
    
    max2 = 0
    
    for num in numbers:
        if num > max2:
            max2 = num
            
    return max * max2