def solution(n):
    answer = []
    answer.append(n)
    for _ in range(1001):
        if n==1:
            break
        if n%2==0:
            n=n//2
            answer.append(n)
        elif n%2==1:
            n=3*n+1
            answer.append(n)
            
    return answer