from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리를 건너는 트럭을 저장할 큐
    bridge = deque([0] * bridge_length)
    # 현재 다리 위의 트럭 총 무게
    current_weight = 0
    # 시간 카운트
    time = 0
    # 대기 중인 트럭 리스트
    index = 0
    
    while index < len(truck_weights):
        # 다리에서 트럭이 나가면
        current_weight -= bridge.popleft()
        
        # 새로운 트럭이 다리에 올라갈 수 있는지 확인
        if current_weight + truck_weights[index] <= weight:
            # 트럭을 다리에 올리고 무게 추가
            bridge.append(truck_weights[index])
            current_weight += truck_weights[index]
            index += 1  # 다음 트럭으로 이동
        else:
            # 트럭이 다리에 올라갈 수 없으면 빈 공간(0)을 추가
            bridge.append(0)
        
        # 시간 증가
        time += 1
        
    # 마지막 트럭이 다리를 건너는 시간을 추가
    return time + bridge_length