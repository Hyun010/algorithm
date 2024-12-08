def solution(l, r):
    answer = []
    for i in range(l,r+1):
        p=True
        for j in str(i):
            if j not in ['0','5']:
                p=False
        if p==True:        
            answer.append(i)
    if answer==[]:
        answer.append(-1)
    return answer