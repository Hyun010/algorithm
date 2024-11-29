def solution(n, results):
    graph = [[0] * (n + 1) for _ in range(n + 1)] #초기화
    for winner, loser in results: #그래프 반영
        graph[winner][loser] = 1 #winner 이김
        graph[loser][winner] = -1 #loser가 winner에게 패함
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1 #i가 j를 이김
                elif graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1 #i가 j에게 패함
    answer = 0
    for i in range(1, n + 1):
        known_results = 0 #알고 있는 경기 결과 수
        for j in range(1, n + 1):
            if graph[i][j] != 0: #i,j 관계O
                known_results += 1
        #모든선수 관계O
        if known_results == n - 1:
            answer += 1
    return answer