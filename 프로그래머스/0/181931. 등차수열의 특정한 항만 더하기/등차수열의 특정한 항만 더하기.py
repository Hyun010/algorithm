def solution(a, d, included):
    answer = 0
    max=a+d*len(included)+1
    numli=[]
    for i in range(a,max,d):
        numli.append(i)
    for i,boo in enumerate(included):
        if boo==True:
            answer+=numli[i]
    return answer