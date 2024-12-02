def solution(score):
    answer = []
    temp=[]
    for i in range(len(score)):
        s=sum(score[i])
        temp.append(s)
    sort_s=sorted(temp, reverse=True)
    answer=[sort_s.index(s)+1 for s in temp]
    return answer