def solution(absolutes, signs):
    answer = 0
    temp=[]
    for i,sign in enumerate(signs):
        if sign==True:
            temp.append(absolutes[i])
        else:
            temp.append(-absolutes[i])
    answer=sum(temp)
    return answer