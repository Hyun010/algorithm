from collections import defaultdict

def solution(info, edges):
    answer = 0
    #트리 구조 생성
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    #DFS 함수 정의
    def dfs(current_node, sheep, wolf, possible_nodes):
        nonlocal answer
        #현재 노드의 정보 업데이트
        if info[current_node] == 0: #양인 경우
            sheep += 1
        else: #늑대인 경우
            wolf += 1
        #조건: 늑대의 수가 양의 수를 초과하면 경로 종료
        if wolf >= sheep:
            return
        #최대 양의 수 갱신
        answer = max(answer, sheep)
        #다음 이동 가능한 노드 리스트 업데이트
        new_possible_nodes = possible_nodes[:]
        new_possible_nodes.remove(current_node)
        new_possible_nodes.extend(graph[current_node])

        #가능한 모든 노드로 DFS 재귀 호출
        for next_node in new_possible_nodes:
            dfs(next_node, sheep, wolf, new_possible_nodes)
    #DFS 시작: 루트 노드(0)에서 시작
    dfs(0, 0, 0, [0])
    return answer