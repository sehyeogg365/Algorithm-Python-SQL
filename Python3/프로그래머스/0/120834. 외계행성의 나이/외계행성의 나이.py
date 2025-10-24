def solution(age):
    answer = ''
    
    strAge = str(age)
    
    for i in strAge:
        if i == '0':
            answer += 'a'
        
        if i == '1':
            answer += 'b'
        
        if i == '2':
            answer += 'c'
            
        if i == '3':
            answer += 'd'
            
        if i == '4':
            answer += 'e'
            
        if i == '5':
            answer += 'f'
            
        if i == '6':
            answer += 'g'
    
        if i == '7':
            answer += 'h'
        
        if i == '8':
            answer += 'i'
            
        if i == '9':
            answer += 'j'
            
    return answer