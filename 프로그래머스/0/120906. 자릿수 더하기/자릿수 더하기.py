def solution(n):
    answer = 0
    nl=list(map(int,str(n)))
    for num in nl:
        answer+=num
    return answer