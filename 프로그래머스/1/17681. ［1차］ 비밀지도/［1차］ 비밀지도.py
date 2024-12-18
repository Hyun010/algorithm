def b(bin):
    t=[]
    for i in str(bin):
        t.append(i)
    t=t[::-1]
    a=0
    for i,num in enumerate(t):
        if num=='1':
            a+=2**i
    return a

def b_m(bin):
    a=''
    while bin>=1:
        a+=str((bin%2))
        bin=bin//2
    a=a[::-1]
    return a

def solution(n, arr1, arr2):
    answer = []
    t1=[]
    t2=[]
    for num in arr1:
        t1.append(b_m(num))
    for i,t in enumerate(t1):
        if len(t)<n:
            t1[i]=t1[i].zfill(n)
    for num in arr2:
        t2.append(b_m(num))
    for i,t in enumerate(t2):
        if len(t)<n:
            t2[i]=t2[i].zfill(n)
    for i in range(n):
        answer.append(b_m(b(t1[i])|b(t2[i])))
    for i,t in enumerate(answer):
        if len(t)<n:
            answer[i]=answer[i].zfill(n)
    for i in range(len(answer)):
        answer[i]=answer[i].replace("1","#").replace("0"," ")
    return answer