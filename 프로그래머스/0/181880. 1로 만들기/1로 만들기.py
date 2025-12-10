def solution(num_list):
    count = 0 
    
    # for문안에 while문 도는 형식으로 바꾸기 
    for i in range(len(num_list)):
        current_num = num_list[i] # 현재 인덱스 원소 꼭 변수처리 
        while current_num > 1:       
            if current_num % 2 == 0: # 짝수라면 반으로 나누고
                current_num = current_num // 2 
            else: # 홀수라면 1을 뺀 뒤 반으로 나눔
                current_num = (current_num - 1) // 2   
                
            count += 1 
                                 
    return count