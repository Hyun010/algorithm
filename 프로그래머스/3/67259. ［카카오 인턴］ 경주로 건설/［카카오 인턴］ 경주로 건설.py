from collections import deque

def solution(board):
    n = len(board)
    INF = 10**9 #최대값
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #우하좌상
    dp = [[[INF] * 4 for _ in range(n)] for _ in range(n)] #각 방향 최소비용 저장
    queue = deque([(0, 0, -1, 0)]) #x,y,방향,비용
    for i in range(4): #시작점 비용을 모든 방향에서 0 초기ㅗ하
        dp[0][0][i] = 0

    while queue:
        x, y, prev_dir, cost = queue.popleft() #현재 좌표, 방향, 비용
        
        for new_dir, (dx, dy) in enumerate(directions): #새로운 방향
            nx, ny = x + dx, y + dy
            #경계 내, 0인 경우만 이동
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = cost + (100 if prev_dir == new_dir or prev_dir == -1 else 600) #비용 계산
                if new_cost < dp[nx][ny][new_dir]: #새 비용이 적으면 DP 갱신 큐 추가
                    dp[nx][ny][new_dir] = new_cost #새 비용
                    queue.append((nx, ny, new_dir, new_cost)) #다음 방향 추가
    return min(dp[n-1][n-1])