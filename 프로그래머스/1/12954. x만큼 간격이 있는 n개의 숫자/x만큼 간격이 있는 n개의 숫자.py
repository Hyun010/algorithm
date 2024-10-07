def solution(x, n):
    answer = []
    if x == 0: #x=0
        answer = [0] * n #n개 0 리스트 반환
    else:
        if x > 0: #x가 양수
            for i in range(n):
                answer.append(x * (i + 1))
        else: #x가 음수
            for i in range(n):
                answer.append(x * (i + 1))
    return answer