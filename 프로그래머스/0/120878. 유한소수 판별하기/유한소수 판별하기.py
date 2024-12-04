def num(n):
    a=[]
    d=2
    while d<=n:
        if n%d !=0:
            d+=1
        else:
            if d not in a:
                a.append(d)
            n//=d
    return a

def gcd(a, b): # 최대공약수
   while b > 0:
       a, b = b, a % b
   return a

def solution(a, b):
    answer = 0
    a,b=a//gcd(a,b), b//gcd(a,b)
    if all(x in [2,5] for x in num(b)):
        answer=1
    else:
        answer=2
    return answer