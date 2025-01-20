from itertools import permutations

def solution(n, weak, dist):
    #취약 지점을 2배로 확장하여 원형을 선형으로 변환
    weak_len = len(weak)
    weak = weak + [w + n for w in weak]
    
    #필요한 최소 친구 수 초기화 (불가능할 경우 대비)
    answer = len(dist) + 1

    #모든 취약 지점에서 시작점을 변경하며 탐색
    for start in range(weak_len):
        #친구 순열을 모두 시도 (최소 인원 탐색)
        for friends in permutations(dist):
            count = 1 #투입할 친구 수
            position = weak[start] + friends[count - 1] #첫 번째 친구가 점검할 수 있는 위치
            #모든 취약 지점 확인
            for index in range(start, start + weak_len):
                if weak[index] > position: #커버 불가 시 다음 친구 투입
                    count += 1
                    if count > len(dist): #모든 친구 사용해도 불가능
                        break
                    position = weak[index] + friends[count - 1]
            #현재 최소 인원보다 작은 경우 갱신
            answer = min(answer, count)
    return answer if answer <= len(dist) else -1
