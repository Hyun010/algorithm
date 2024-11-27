def b(bin):
    a=0
    t = []
    for i in str(bin):
        t.append(i)
    t = t[::-1]
    for i,num in enumerate(t):
        if num=='1':
            a+=3**i
        elif num == '2':
            a += 2*(3 ** i)
    return a

def solution(n):
    answer = 0
    temp=''
    while True:
        if n<1:
            break
        temp+=str(n%3)
        n=n//3
    answer=b(temp)
    return answer