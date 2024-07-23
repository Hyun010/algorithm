def solution(money):
    answer = []
    cnt=money//5500
    extra=money%5500
    answer.append(cnt)
    answer.append(extra)
    return answer