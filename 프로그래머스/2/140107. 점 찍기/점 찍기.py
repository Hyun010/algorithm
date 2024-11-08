def solution(k, d):
    answer = 0
    for a in range(d // k + 1): #x 개수
        max_y = (d**2 - (a * k)**2)**0.5 #거리계산 공식으로 최대 y계산
        answer += int(max_y // k) + 1 #y 개수
    return answer