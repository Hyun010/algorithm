def solution(n):
    answer = 0
    if float(n**(1/2)).is_integer()==True:
        answer=1
    else:
        answer=2
    return answer