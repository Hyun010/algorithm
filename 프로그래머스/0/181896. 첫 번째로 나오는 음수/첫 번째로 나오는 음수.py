def solution(num_list):
    answer = 0
    for i,num in enumerate(num_list):
        if num<0:
            answer=i
            break
        else:
            answer=-1
    return answer