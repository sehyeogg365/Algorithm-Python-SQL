def solution(emergency):
    # 1. 내림차순 정렬 (순위 매길 기준 준비)
    sorted_emergency = sorted(emergency, reverse=True) 
    print(sorted_emergency)
    # 2. {응급도 값: 순위} 딕셔너리 생성
    rank_map = {}
    # enumerate를 사용하여 인덱스(0, 1, 2...)를 순위(1, 2, 3...)로 활용
    for index, value in enumerate(sorted_emergency):
        rank_map[value] = index + 1 # 순위는 1부터 시작
       
    print(rank_map)
    # 3. 원본 리스트를 순회하며 순위로 변환
    answer = []
    for val in emergency:
        # 딕셔너리에서 해당 값의 순위를 찾아서 리스트에 추가
        answer.append(rank_map[val])
    print(answer)    
    return answer
