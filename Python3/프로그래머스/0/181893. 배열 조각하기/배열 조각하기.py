def solution(arr, query):
    answer = []
    
    for i in range(len(query)):
        q_idx = query[i]
        if i % 2 == 0:# 짝수 인덱스에서는
            del arr[q_idx + 1: ]
            answer.append(arr)
            #  arr에서 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
        else: # 홀수 인덱스 arr에서
            del arr[ :q_idx]
            answer.append(arr)
                # query[i]번 인덱스 앞부분을 잘라서 버립니다.

    return arr