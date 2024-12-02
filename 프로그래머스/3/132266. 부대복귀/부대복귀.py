from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    #그래프 그리기(길)
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    #BFS 사용
    def bfs(start):
        queue = deque([start])
        distances = {i: -1 for i in range(1, n + 1)} #거리 초기화
        distances[start] = 0 #시작거리 0
        while queue:
            current = queue.popleft()
            current_distance = distances[current]
            for neighbor in graph[current]:
                if distances[neighbor] == -1: #방문하지 않은 노드
                    distances[neighbor] = current_distance + 1
                    queue.append(neighbor)
        return distances
    distance_map = bfs(destination) 
    answer = [distance_map[source] for source in sources]
    return answer