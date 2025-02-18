import heapq

def solution(n, paths, gates, summits):
    #그래프 초기화
    graph = {i: [] for i in range(1, n + 1)}
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    #출입구와 산봉우리 구분 (set 사용하여 빠른 검색)
    summit_set = set(summits)
    gate_set = set(gates)
    #다익스트라 변형: 최소 intensity를 찾기 위한 우선순위 큐
    intensity = [float('inf')] * (n + 1) #최소 intensity 저장
    pq = [] #(현재 intensity, 현재 노드)
    #출입구에서 시작하는 다익스트라 초기화
    for gate in gates:
        heapq.heappush(pq, (0, gate))
        intensity[gate] = 0
    #다익스트라 탐색 (intensity 기준)
    while pq:
        max_time, node = heapq.heappop(pq)
        #이미 더 작은 intensity로 방문된 경우 무시
        if max_time > intensity[node]:
            continue
        #산봉우리에 도달한 경우, 더 탐색할 필요 없음
        if node in summit_set:
            continue
        #현재 노드에서 이동 가능한 모든 노드 탐색
        for neighbor, cost in graph[node]:
            if neighbor in gate_set: #출입구로 돌아가는 경로는 고려하지 않음
                continue
            new_intensity = max(max_time, cost)
            #더 작은 intensity로 방문 가능하면 갱신
            if intensity[neighbor] > new_intensity:
                intensity[neighbor] = new_intensity
                heapq.heappush(pq, (new_intensity, neighbor))
    #최적의 산봉우리 찾기
    best_summit = (-1, float('inf')) #(산봉우리 번호, 최소 intensity)
    for summit in summits:
        if intensity[summit] < best_summit[1]:
            best_summit = (summit, intensity[summit])
        elif intensity[summit] == best_summit[1] and summit < best_summit[0]:
            best_summit = (summit, intensity[summit])
    return list(best_summit)
