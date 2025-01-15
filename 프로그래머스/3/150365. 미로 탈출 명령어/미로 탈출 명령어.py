import sys
sys.setrecursionlimit(5000)

def solution(n, m, x, y, r, c, k):
    answer = []
    #방향 정의 (사전 순: l, r, u, d)
    directions = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    #맨해튼 거리 계산
    distance = abs(x - r) + abs(y - c)
    if distance > k or (k - distance) % 2 != 0:
        return "impossible"
    #DFS로 경로 탐색
    def dfs(current_x, current_y, remaining_k, path):
        #목표 도달 및 조건 만족
        if remaining_k == 0:
            if (current_x, current_y) == (r, c):
                answer.append(path)
            return
        #사전 순 탐색
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            #격자 내 이동 가능 확인
            if 1 <= nx <= n and 1 <= ny <= m:
                #가지치기: 최소 거리 계산
                if abs(nx - r) + abs(ny - c) <= remaining_k - 1:
                    dfs(nx, ny, remaining_k - 1, path + directions[i])
                    #경로가 이미 발견되었으면 종료
                    if answer:
                        return
    #DFS 시작
    dfs(x, y, k, "")
    return answer[0] if answer else "impossible"