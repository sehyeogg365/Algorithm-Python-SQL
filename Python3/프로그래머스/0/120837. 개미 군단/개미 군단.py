def solution(hp):
    answer = 0
    # 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력
    count = 0
  
    answer += hp // 5 # hp = 23이면 장군개미 4마리가 필요
    hp = hp - (hp - (hp % 5)) # hp 그러면 23 - 20 이 깎여야 함   
    
    answer += hp // 3 # hp = 3 남은 상태 병정개미 1마리 필요
    hp = hp - (hp - (hp % 3)) # hp 3 - 3이 깍여야 함 

    answer += hp // 1
    hp = hp - (hp - (hp % 1))
    
    return answer