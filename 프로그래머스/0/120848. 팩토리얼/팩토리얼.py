def my_factorial(n):
    if(n > 1):
        return n * my_factorial(n - 1)
    else:
        return 1

def solution(n):
    answer = 0
    for i in range(11):
        if my_factorial(i)<=n:
            answer=i
    return answer