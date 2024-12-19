def solution(n):
    cnt=1 # 처음 한칸 이동
    while n>1:
        if n%2==0:
            n=n/2
        else:
            n=n-1
            cnt+=1
    return cnt