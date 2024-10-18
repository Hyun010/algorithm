from collections import deque

def solution(n, edges):
    graph = [[] for _ in range(n + 1)] #그래프 초기화
    for a, b in edges: #그래프 연결
        graph[a].append(b)
        graph[b].append(a)
    #BFS를 위한 큐와 방문 리스트 초기화
    queue = deque([1]) #1번 노드 출발 큐 생성
    visited = [False] * (n + 1) #방문 여부
    visited[1] = True #시작노드 방문
    while queue:
        current_level_nodes = len(queue) #현재레벨의 노드개수
        answer = 0 #먼 거리 개수
        for _ in range(current_level_nodes): #현재 레벨 노드 탐색
            node = queue.popleft() #노드 추출
            
            for neighbor in graph[node]: #인접노드 탐색
                if not visited[neighbor]: #방문X
                    visited[neighbor] = True #방문처리
                    queue.append(neighbor) #큐에 추가
        # 현재 레벨의 노드 수가 0보다 크면 가장 멀리 떨어진 노드 수 증가
        if current_level_nodes > 0:
            answer = current_level_nodes
    return answer