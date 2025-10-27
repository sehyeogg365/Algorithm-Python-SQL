def solution(n):
    answer = 0
    # 4, 6, 8, 9, 10, 12, 14, 15
    
    count = 0 # 약수 갯수
    numCount = 0 # 합성수 갯수 
    for i in range(1, n + 1): # 여기선 약수의 갯수를 센다.
        for j in range(1, i + 1): # 합성수 여부 계산    
          if i % j == 0:
            count += 1
            
        # 약수가 3개 이상이면 합성수이다.
        if count >= 3:
            numCount += 1
        
        count = 0
    
    return numCount