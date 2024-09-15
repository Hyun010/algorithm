def solution(array):
    answer = []
    max=0
    idx=0
    for i,num in enumerate(array):
        if max<num:
            max=num
            idx=i
    answer.append(max)
    answer.append(idx)
    return answer