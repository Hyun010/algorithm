def is_prime(n):
    if n<2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    temp='' #진수 변환 담는 곳
    #진수 변환
    while n>0:
        n,mod=divmod(n,k)
        temp=str(mod)+temp
    temp=temp.split('0') #0기준 분할
    #소수 판별
    for i in temp:
        if i and is_prime(int(i)):
            answer+=1
    return answer