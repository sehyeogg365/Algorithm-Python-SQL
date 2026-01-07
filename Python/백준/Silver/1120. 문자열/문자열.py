import sys

# 입력 받기 (sys.stdin.readline은 대량의 데이터를 읽을 때 효율적입니다)
# .split()을 사용해 공백으로 구분된 A와 B를 가져옵니다.
A, B = sys.stdin.readline().split()

# 최종 최소 차이를 저장할 변수 (최대값인 A의 길이로 초기화)
min_diff = len(A)

# A를 B의 어느 위치에 둘지 결정하는 반복문
# i는 B에서 A가 시작되는 인덱스입니다.
for i in range(len(B) - len(A) + 1):
    current_diff = 0
    
    # A와 B의 부분 문자열을 비교
    for j in range(len(A)):
        if A[j] != B[i + j]:
            current_diff += 1
            
    # 가장 작은 차이값을 갱신
    if current_diff < min_diff:
        min_diff = current_diff

print(min_diff)