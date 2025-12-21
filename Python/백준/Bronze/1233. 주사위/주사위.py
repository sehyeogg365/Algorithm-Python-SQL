S1, S2, S3 = map(int, input().split())

def Solution(S1, S2, S3):
    '''
    주사위1은 S1(3)개의 면이 있으므로 1, 2, 3의 눈을 가지고
    , 주사위2는 S2(2)개의 면이 있으므로 1, 2의 눈을 가지며
    , 주사위3은 S3(3)개의 면이 있으므로 1, 2, 3의 눈을 가진다
    '''
    # 가장 많이 발생하는 합을 구하는 것이다.
    # 빈도수 저장 = 딕셔너리 사용
    dict1 = {}

    list_s1 = []
    list_s2 = []
    list_s3 = []
    # 리스트 화 
    for i in range(1, S1+1):
        list_s1.append(i)

    for i in range(1, S2+1):
        list_s2.append(i)

    for i in range(1, S3+1):
        list_s3.append(i)

    
    for x in list_s1:
        for y in list_s2:
            for z in list_s3:
                # print(x, y, z)
                sum = x + y + z
                if sum in dict1:
                    dict1[sum] += 1 # 원래 저장된 합(키)이면 +1
                else:
                    dict1[sum] = 1 # 키값이 없다면 1저장

    # 반복문을 써서 찾아본다.
    answer = 0
    max_freq = 0

    # dict1의 키(합)들을 작은 순서대로 확인
    for s in sorted(dict1.keys()): # 키 값 
        if dict1[s] > max_freq:
            max_freq = dict1[s]# 최대 빈도 갱신
            answer = s # 그때의 합 

    # max_value = max(dict1.values()) # 최다 빈도수인 키 값
    return answer

print(Solution(S1, S2, S3))





