def solution(n):
    cnt=0
    cnt_total=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i%j==0:
                cnt+=1
            elif i==j:
                break
        if cnt>=3:
            cnt_total+=1
            cnt=0
        else:
            cnt=0
    return cnt_total