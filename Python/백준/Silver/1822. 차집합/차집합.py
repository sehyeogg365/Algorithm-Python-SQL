'''
몇 개의 자연수로 이루어진 두 집합 A와 B가 있다. 집합 A에는 속하면서 집합 B에는 속하지 않는 모든 원소를 구하는 프로그램을 작성하시오.

첫째 줄에는 집합 A의 원소의 개수 n(A)와 집합 B의 원소의 개수 n(B)가 빈 칸을 사이에 두고 주어진다. 
(1 ≤ n(A), n(B) ≤ 500,000)이 주어진다.
 둘째 줄에는 집합 A의 원소가, 셋째 줄에는 집합 B의 원소가 빈 칸을 사이에 두고 주어진다. 
 하나의 집합의 원소는 2,147,483,647 이하의 자연수이며, 
하나의 집합에 속하는 모든 원소의 값은 다르다.
'''
import sys


# 1,5
# a = set([1,2, 3, 7])
# b = set([1, 1, 2, 3, 4])

input = sys.stdin.read
data = input().split()

a = int(data[0])# 갯수 입력
b = int(data[1])# 갯수 입력 

def set_definiation(a, b):

    # 1. 집합 A 만들기 (2번 인덱스부터 a개만큼)
    set_a = set(map(int, data[2 : 2+a]))

    # 2. 집합 B 만들기 (2+a번 인덱스부터 끝까지)
    set_b = set(map(int, data[2+a : ]))

    diff = sorted(list(set_a - set_b))
    length = len(diff)
    if length > 0:
        result_set = diff

    return length, diff

count, result = set_definiation(a, b)
print(count)
if count > 0:
    print(*(result))