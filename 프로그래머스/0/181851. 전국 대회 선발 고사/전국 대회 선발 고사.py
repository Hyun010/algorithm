def solution(rank, attendance):
    answer = 0
    temp=[]
    t=[]
    s=[]
    for i in range(len(attendance)):
        if attendance[i]==True:
            temp.append(i)
            t.append(rank[i])
    for i in range(3):
        idx=t.index(min(t))
        s.append(temp[idx])
        t[idx]=max(t)+1
    a,b,c=s[0],s[1],s[2]
    answer=10000*a+100*b+c
    return answer