def solution(targets):
    targets.sort(key=lambda x: x[1]) #끝점에 맞춰서 정렬
    answer = 0
    last_interception = -1 #마지막 요격 미사일의 위치
    for start, end in targets:
        #현재 구간이 마지막 요격 미사일로 커버되지 않으면 새로운 요격 필요
        if start >= last_interception:
            answer += 1
            last_interception = end #현재 구간의 끝점에 요격 미사일 배치
    return answer