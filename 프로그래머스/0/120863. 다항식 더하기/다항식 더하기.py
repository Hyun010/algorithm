def solution(polynomial):
    answer=''
    t = []
    s = []
    p = []
    polynomial = polynomial.split(' + ')
    for str in polynomial:
        if "x" in str:
            if str[0] == "x":
                t.append(1)
            else:
                p=str.split("x")
                t.append(int(p[0]))
        else:
            s.append(int(str))
    su = sum(t)
    su_s=sum(s)
    if su==1:
        if s == [] and t == []:
            answer = '0'
        elif s == []:
            answer = f'x'
        elif t == []:
            answer = f'{su_s}'
        else:
            answer = f'x + {su_s}'
    else:
        if s == [] and t == []:
            answer = '0'
        elif s == []:
            answer = f'{su}x'
        elif t == []:
            answer = f'{su_s}'
        else:
            answer = f'{su}x + {su_s}'
    return answer