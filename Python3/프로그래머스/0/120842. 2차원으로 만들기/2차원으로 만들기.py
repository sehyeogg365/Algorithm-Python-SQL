def solution(num_list, n):
    answer = [[0 for col in range(n)] for row in range(int(len(num_list)/n))]
    print(answer)
    
    idx = 0
    row = len(num_list)//n
    col = n
    # 배열 길이 8이고 n = 2이면 2 * 4배열로 변경 해야 한다.
    # 행 두개로 변경하기 idx 라는 변수 추가 반복문 밖에, 행, 열 변수도 따로 만들기 
    for i in range(row):  # 행
        for j in range(col): # 열
            answer[i][j] = num_list[idx]
            idx+=1
    
    return answer