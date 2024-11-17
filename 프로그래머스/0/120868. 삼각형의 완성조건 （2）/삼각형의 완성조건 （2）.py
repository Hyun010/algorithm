def solution(sides):
    a=0
    b=0
    cnt=0
    s=[]
    if sides[0]>=sides[1]:
        a,b=sides[0],sides[1]
    else:
        a,b=sides[1],sides[0]
    for i in range(1,a+1):
        #a일경우 a<b+i
        if a<b+i:
            cnt+=1
    for i in range(a+1,a+b+1):
        #i일 경우 i<a+b
        if i<a+b:
            cnt+=1
    return cnt