def solution(cards1, cards2, goal):
    answer = ''
    idx1=0
    idx2=0
    t=[]
    for g in goal:
        if g==cards1[idx1]:
            t.append(cards1[idx1])
            if idx1<(len(cards1)-1):
                idx1+=1
        elif g==cards2[idx2]:
            t.append(cards2[idx2])
            if idx2<(len(cards2)-1):
                idx2+=1
        else:
            break
    if t==goal:
        answer+='Yes'
    else:
        answer+='No'
    return answer