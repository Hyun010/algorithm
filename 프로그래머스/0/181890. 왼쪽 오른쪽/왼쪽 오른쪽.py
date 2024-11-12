def solution(str_list):
    l_answer = []
    r_answer=[]
    for i,str in enumerate(str_list):
        if str=='u' or str=='d':
            l_answer.append(str)
        elif str=='l':
            return l_answer
        elif str=='r':
            r_answer=str_list[i+1:]
            return r_answer
    if len(l_answer)==len(str_list):
        answer=[]
    return answer