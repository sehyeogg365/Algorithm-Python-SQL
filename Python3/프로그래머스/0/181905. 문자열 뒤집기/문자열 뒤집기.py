def solution(my_string, s, e):
    answer = ''  
    
    reverse_str = ""
    reverse_str = list(my_string[s:e+1])
    reverse_str.reverse() # 리스트로 변환해야 reverse() 사용 가능
    reverse_str = "".join(reverse_str) # 뒤집힌 '리스트'를 다시 '하나의 문자열'로 합치기

    return my_string[0:s] + reverse_str + my_string[e+1:]