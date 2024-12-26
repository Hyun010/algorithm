def solution(array):
    answer = 0
    t=[0]*1001
    for i in array:
        t[i]+=1
    m=max(t)
    if t.count(m)>1:
        return -1
    answer=t.index(m)
    return answer