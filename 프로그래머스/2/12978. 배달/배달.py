import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)] #그래프 초기화
    for a, b, c in road: #양방향 도로 설정
        graph[a].append((b, c))
        graph[b].append((a, c))

    distances = [float('inf')] * (N + 1) #최단 거리 초기화
    distances[1] = 0 #1번 마을 거리 초기화
    queue = [(0, 1)]  # (거리, 마을 번호), 우선순위 큐 초기화

    while queue:
        current_distance, current_town = heapq.heappop(queue)
        #최단거리 조건
        if current_distance > distances[current_town]:
            continue
        #인접한 마을 탐색
        for neighbor, travel_time in graph[current_town]:
            distance = current_distance + travel_time
            #더 짧은 경로가 발견되면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    answer = sum(1 for d in distances[1:] if d <= K) #조건 맞는 마을 개수 합
    
    return answer