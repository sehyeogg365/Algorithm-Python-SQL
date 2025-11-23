n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 최대 동전 수를 저장할 변수 초기화
max_coins = 0

# 1. 3x3 부분 격자의 시작점 (i, j)을 순회하는 외부 반복문
# 범위는 0부터 N-3까지 (N-2까지 반복)
# grid[i][j]가 3x3 격자의 좌측 상단 모서리가 됨
for i in range(n - 2): 
    for j in range(n - 2):
        # 현재 3x3 격자의 동전 수를 저장할 변수 초기화
        current_coins = 0
        
        # 2. 현재 시작점 (i, j)을 기준으로 3x3 영역을 순회하는 내부 반복문
        # 행: i부터 i+2까지, 열: j부터 j+2까지
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                # 동전이 있다면 (값이 1이라면) current_coins에 더함
                # if grid[r][c] == 1:
                #     current_coins += 1
                # 1 또는 0이므로, 바로 더하는 것이 더 효율적입니다.
                current_coins += grid[r][c]
        
        # 3. 최대 동전 수 업데이트
        # 현재 3x3 영역의 동전 수가 지금까지의 최대값보다 크다면 업데이트
        if current_coins > max_coins:
            max_coins = current_coins

print(max_coins)