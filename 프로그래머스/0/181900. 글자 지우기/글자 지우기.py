def solution(my_string, indices):
    answer = ''
    for i,str in enumerate(my_string):
        if i in indices:
            pass
        else:
            answer+=str
    return answer