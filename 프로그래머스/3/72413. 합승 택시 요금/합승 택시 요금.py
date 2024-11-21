import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)] #그래프 초기화
    #그래프 생성(양방향)
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    def dijkstra(start):
        distances = [float('inf')] * (n + 1) #최단거리 초기화
        distances[start] = 0 #시작 초기화
        priority_queue = [(0, start)] #(비용,노드)
        while priority_queue:
            current_cost, current_node = heapq.heappop(priority_queue)
            #현재비용>이미기록된 비용(최저 비용을 위해) 패스
            if current_cost > distances[current_node]:
                continue
            #탐색
            for neighbor, fare in graph[current_node]:
                new_cost = current_cost + fare
                #새로운 비용이 적으면 업데이트
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
        return distances #최단거리 맞춰 코스트 저장
    #출발점에서 나머지 노드까지 거리
    distances_from_s = dijkstra(s)
    distances_from_a = dijkstra(a)
    distances_from_b = dijkstra(b)
    #각자 가는 경우 최소비용
    answer = distances_from_s[a] + distances_from_s[b]

    #합승을 고려한 비용 계산
    for i in range(1, n + 1):
        if distances_from_s[i] < float('inf'):
            cost = distances_from_s[i] + distances_from_a[i] + distances_from_b[i]
            answer = min(answer, cost) #각자 가는 경우 vs 새로운 비용 최소 선택
    return answer