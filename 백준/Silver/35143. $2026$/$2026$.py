import sys

# 자릿수 N 입력
N = int(sys.stdin.readline())

# 1. sqrt(X_N)에 해당하는 M의 자릿수 구하기
# N=3 -> M=2자리(11), N=5 -> M=3자리(101)
m_len = (N + 1) // 2

# 2. M 생성 (가장 작은 팰린드롬 형태: 100...001)
if m_len == 1:
    # N=1인 경우 (사실상 1자리 특별한 수는 1 뿐임)
    M = 1
else:
    # 맨 앞 1, 중간에 0이 (m_len-2)개, 맨 뒤 1
    M_str = '1' + '0' * (m_len - 2) + '1'
    M = int(M_str)

# 3. 특별한 수 X_N은 M의 제곱
X_N = M ** 2

# 4. 고려대 개교 연도(1905)에 X_N 주년을 더함
ans = 1905 + X_N

print(ans)