import math

def solution(n):
    answer = 0
    
    sqrt_number = math.sqrt(n)
    if int(sqrt_number) == sqrt_number:
        answer = 1
    else :
        answer = 2
        
    return answer