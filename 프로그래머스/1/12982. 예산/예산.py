def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        budget-=d[i]
        answer+=1
        if budget==0:
            break
        elif budget<0:
            answer-=1
            break
    return answer