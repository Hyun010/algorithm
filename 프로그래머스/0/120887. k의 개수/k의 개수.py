def solution(i, j, k):
    answer = 0
    temp=[]
    for l in range(i,j+1):
        temp.append(str(l))
    for l in temp:
        answer+=l.count(str(k))
    return answer