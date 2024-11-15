def facto(n):
    if(n > 1):
        return n * facto(n - 1)
    else:
        return 1

def solution(balls, share):
    answer = 0
    answer=facto(balls)/(facto(balls-share)*facto(share))
    return answer