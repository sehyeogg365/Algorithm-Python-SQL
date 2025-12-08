def solution(todo_list, finished):
    answer = []
    
    for i in range(len(todo_list)): # todo_list 인덱스 내 원소가 finishsed 인덱스 내 원소 비교 
        if not finished[i]:
            answer.append(todo_list[i])
        
    return answer