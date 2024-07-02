def solution(n, computers):
    answer = 0
    network_list=[[] for i in range(n)] #한 컴퓨터에 연결된 컴퓨터 리스트
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]==1: #컴퓨터 연결이 되어있다면
                network_list[i].append(j) #연결
                network_list[j].append(i) #상호 연결
    visited=[] #방문했는지 체크 스택
    def dfs(v,visited,network_list): #깊이우선탐색
        if v not in visited: #방문 체크
            visited.append(v) #네트워크 연결 추가
        for i in network_list[v]: #한 네트워크 연결시키는 곳
            if i not in visited: #네트워크 연결이 없다면
                visited=dfs(i,visited,network_list) #방문 최신화, 네트워크 연결
        return visited
    for i in range(n):
        if i not in visited: #네트워크 시작
            visited=dfs(i,visited,network_list) #네트워크 연결
            answer+=1 #네트워크 연결 완료
    return answer