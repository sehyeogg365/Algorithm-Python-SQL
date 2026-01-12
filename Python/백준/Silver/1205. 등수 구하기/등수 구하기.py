import sys

# 1. 입력 받기 (N: 현재 개수, new_score: 태수 점수, P: 랭킹 제한)
# sys.stdin.readline을 쓰면 더 빠르고 안전합니다.
line = sys.stdin.readline().split()
if not line:
    exit() # 입력이 없으면 종료

n, new_score, p = map(int, line)

# 2. N이 0이라면? (예외 처리)
if n == 0:
    print(1)
    exit()

# 3. 현재 랭킹 리스트 입력 받기
scores = list(map(int, sys.stdin.readline().split()))

# 4. 랭킹 진입 가능 여부 확인
# 리스트가 꽉 찼는데(n == p), 맨 마지막 점수보다 내 점수가 작거나 같으면 진입 불가
if n == p and scores[-1] >= new_score:
    print(-1)
else:
    # 5. 등수 계산 (나보다 점수 높은 사람 수 + 1)
    res = 1
    for s in scores:
        if s > new_score:
            res += 1
        else:
            break
    print(res)