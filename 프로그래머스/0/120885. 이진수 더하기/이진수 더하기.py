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

def solution(bin1, bin2):
    answer = ''
    if bin1=='0' and bin2=='0':
        answer='0'
    else:
        b1=b(bin1)
        b2=b(bin2)
        s=b1+b2
        answer=b_m(s)
    print(answer)
    return answer