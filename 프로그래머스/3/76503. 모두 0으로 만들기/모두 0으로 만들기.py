import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def solution(a, edges):
    #만약 전체 가중치의 합이 0이 아니라면 불가능
    if sum(a) != 0:
        return -1
    #그래프를 인접 리스트 형태로 변환
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    #방문 여부 및 이동 횟수 저장 변수
    visited = [False] * len(a)
    answer = 0 #최소 이동 횟수 저장 변수
    def dfs(node):
        """ DFS를 이용하여 자식 노드에서 부모 노드로 가중치를 전달하는 함수 """
        nonlocal answer
        visited[node] = True
        total_weight = a[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                weight_from_child = dfs(neighbor) #자식 노드에서 전달된 가중치
                answer += abs(weight_from_child) #이동 횟수 누적
                total_weight += weight_from_child #현재 노드의 가중치 업데이트
        return total_weight #부모 노드에 전달할 가중치
    #DFS 탐색 시작 (0번 노드를 루트로 가정)
    dfs(0)
    return answer
