from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list) #항공권 정보 딕셔너리
    for start, end in tickets: #그래프 초기화
        graph[start].append(end)
    for key in graph:
        graph[key].sort() #각 출발지-도착지 알파벳 순 정렬
    #DFS 함수 정의
    def dfs(airport):
        while graph[airport]:#현재 가능한 모든 도착지를 순회
            next_airport = graph[airport].pop(0) #가장 앞 공항 빼기
            dfs(next_airport) #재귀
        answer.append(airport) #모든 공항 방문 후 루트 저장
    dfs("ICN") #시작
    
    return answer[::-1] #경로 역순반환(DFS 특성상 역순 저장)