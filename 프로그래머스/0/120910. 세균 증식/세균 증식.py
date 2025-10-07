def solution(n, t):
    answer = 1
    for i in range(1, t+1):  
        answer = n * (2 ** i)
        
    return answer