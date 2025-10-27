def solution(my_string):
    answer = ''
    
    data = []
    for i in my_string:
        data.append(i)
        
    print(data)    
    
    unique_dict = dict.fromkeys(data)
    
    result_list = list(unique_dict.keys())
    
    for i in result_list:
        answer += i

    return answer