def solution(str_list, ex):
    answer = ''
    for i,str in enumerate(str_list):
        if ex in str:
            pass
        else:
            answer+=str
    return answer