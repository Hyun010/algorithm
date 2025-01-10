def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups: #남아있으면 루프
        while deliveries and deliveries[-1] == 0: #마지막 0제거
            deliveries.pop()
        while pickups and pickups[-1] == 0: #마지막 0제거
            pickups.pop()
        max_distance = max(len(deliveries), len(pickups)) #멀리있는집 선택
        #배달 작업
        current_cap = cap
        for i in range(len(deliveries) - 1, -1, -1):
            if current_cap == 0: #트럭 용량 소진
                break
            if deliveries[i] > 0: #배달 가능한 경우
                if deliveries[i] <= current_cap:
                    current_cap -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= current_cap
                    current_cap = 0
        #수거 작업
        current_cap = cap
        for i in range(len(pickups) - 1, -1, -1):
            if current_cap == 0: #트럭 용량 소진
                break
            if pickups[i] > 0: #수거 가능한 경우
                if pickups[i] <= current_cap:
                    current_cap -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= current_cap
                    current_cap = 0
        answer += max_distance * 2 #왕복 거리 추가
    return answer