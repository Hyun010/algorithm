def solution(left, right):
    answer = 0
    s=[]
    sc=[]
    cnt=0
    for i in range(left,right+1):
        s.append(i)
    for num in s:
        for i in range(1,num+1):
            if num%i==0:
                cnt+=1
        sc.append(cnt)
        cnt=0
    for i,cnt in enumerate(sc):
        if cnt%2==0:
            answer+=s[i]
        else:
            answer-=s[i]
    return answer