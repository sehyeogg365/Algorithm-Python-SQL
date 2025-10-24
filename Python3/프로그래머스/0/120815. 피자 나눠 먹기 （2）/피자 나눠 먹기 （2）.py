def solution(n):
    answer = 0
    
    for i in range(1, 600):
        if i % n == 0:
            if i % 6 == 0:
                answer = i // 6
                break
        
    return answer