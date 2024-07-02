def solution(n, computers):
    answer = 0
    network_list=[[] for i in range(n)] #네트워크 연결 리스트 초기화
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]==1: #연결이 되어있으면
                network_list[i].append(j) #연결
                network_list[j].append(i) #상호 연결
    visited=[] #방문했는지 체크
    def dfs(v,visited,network_list): #깊이우선탐색
        if v not in visited: #방문 체크
            visited.append(v) #방문 안했을 때 했다고 설정
        for i in network_list[v]: #현재 연결된 것들 체크
            if i not in visited: #방문하지 않을 경우
                visited=dfs(i,visited,network_list) #방문 최신화
        return visited
    for i in range(n):
        if i not in visited: #방문하지 않을 경우
            visited=dfs(i,visited,network_list) #방문 최신화
            answer+=1 #네트워크 연결 완료
    return answer