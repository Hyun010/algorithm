def b_m(bin):
    a=''
    while bin>=1:
        a+=str((bin%2))
        bin=bin//2
    a=a[::-1]
    return a


def solution(s):
    cnt=0
    cnt_c=0
    answer = []
    t=[]
    s = list(map(str, str(s)))
    while True:
        for i in s:
            if i=='0':
                cnt+=1
                continue
            else:
                t.append(i)
        s=list(map(str,b_m(len(t))))
        t=[]
        cnt_c+=1
        if s==["1"]:
            break
    answer.append(cnt_c)
    answer.append(cnt)
    return answer