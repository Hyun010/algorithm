def dfs(node, graph, visited):
    visited[node] = True #방문 확인
    count = 1 #현재 노드포함 개수
    for neighbor in graph[node]: #연결된 것 확인
        if not visited[neighbor]: #방문되지 않은 것을 확인될 경우
            count += dfs(neighbor, graph, visited) #다음걸로 끊어 보기
    return count #현재 연결된 개수

def solution(n, wires):
    answer = float('inf') #최소를 위한 최대
    graph = [[] for _ in range(n + 1)] #그래프 표현
    for v1, v2 in wires: #연결 표현
        graph[v1].append(v2)
        graph[v2].append(v1)
    for v1, v2 in wires:
        visited = [False] * (n + 1) #전선 끊음을 확인
        visited[v1] = True #시작 방문 체크
        count_v1 = dfs(v2, graph, visited) #개수
        count_v2 = n - count_v1 #나머지 개수
        difference = abs(count_v1 - count_v2) #차이
        answer = min(answer, difference) #최소치
    return answer