import sys
import math 

# 테스트 케이스의 개수 
T = int(sys.stdin.readline())


# 조규현의 좌표  백승환의 좌표 조규현이 계산한 류재명과의 거리 
# $r1$과 백승환이 계산한 류재명과의 거리 $r2
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)# 유클리드로 거리 구하고 
    sum_r = r1 + r2 
    sub_r = abs(r1 - r2)

    # 일치하는지 여부 분기처리 
    # 두 원이 일치 -1
    if distance == 0 and r1 == r2:
        print(-1)
    # 내접 또는 외접
    elif sum_r == distance or sub_r == distance: 
        print(1)
    # 두 점에서 만남
    elif sub_r < distance < sum_r:
        print(2)
    else :
        print(0)

