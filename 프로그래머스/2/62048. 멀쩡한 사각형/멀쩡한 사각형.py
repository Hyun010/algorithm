#최대공약수
def gcd(a, b):
    while b!=0:
        a,b=b,a%b
    return a

def solution(w,h):
    total=w*h
    unusable_squares=(w+h)-gcd(w, h) #각 가로, 세로에 중복된 것 빼면 사용X
    answer=total-unusable_squares #전체에서 사용X 뺀값
    return answer