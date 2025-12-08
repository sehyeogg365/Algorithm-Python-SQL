def solution(names):
    answer = []
    # 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return
    
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])
        
    
    return answer