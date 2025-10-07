def solution(sides):
    answer = 0
    max = 0 
    sum = 0
    
    for side in sides:
        sum += side # sum변수에 리스트에 요소를 더한다.
        
        # 최대값도 조건문을 통해 구하고
        if side > max: 
            max = side
            
        # 합산된 결과 - 최대값이 최대값보다 클시 작을시 분기처리 
        if sum - max > max:
            answer = 1
        else:
            answer = 2
     
    return answer