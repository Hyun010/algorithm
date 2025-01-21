#최대 공약수 구하기
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    ja=numer1*denom2+numer2*denom1
    mo=denom1*denom2
    answer=[ja//gcd(ja,mo),mo//gcd(ja,mo)]
    return answer