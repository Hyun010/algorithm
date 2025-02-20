from collections import deque

def solution(board):
    N = len(board)
    #이동 가능한 4방향 (상, 하, 좌, 우)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #회전 가능한 경우 (가로 -> 세로, 세로 -> 가로)
    def get_rotations(pos):
        result = []
        (x1, y1), (x2, y2) = pos
        if x1 == x2: #가로 상태 -> 세로 상태 회전 가능
            for dx in [-1, 1]: #위/아래 체크
                if 0 <= x1 + dx < N and 0 <= x2 + dx < N and board[x1 + dx][y1] == 0 and board[x2 + dx][y2] == 0:
                    result.append(((x1, y1), (x1 + dx, y1))) #첫 번째 칸을 축으로 회전
                    result.append(((x2, y2), (x2 + dx, y2))) #두 번째 칸을 축으로 회전
        else: #세로 상태 -> 가로 상태 회전 가능
            for dy in [-1, 1]: #좌/우 체크
                if 0 <= y1 + dy < N and 0 <= y2 + dy < N and board[x1][y1 + dy] == 0 and board[x2][y2 + dy] == 0:
                    result.append(((x1, y1), (x1, y1 + dy))) #첫 번째 칸을 축으로 회전
                    result.append(((x2, y2), (x2, y2 + dy))) #두 번째 칸을 축으로 회전
        return result
    #BFS 탐색
    def bfs():
        queue = deque()
        visited = set()
        start = ((0, 0), (0, 1)) #초기 위치
        queue.append((start, 0)) #(현재 위치, 이동 시간)
        visited.add(start)
        while queue:
            (pos1, pos2), time = queue.popleft()
            if (N - 1, N - 1) in [pos1, pos2]: #목표 지점 도달
                return time
            #1️⃣ 상하좌우 이동
            for dx, dy in moves:
                nxt1, nxt2 = (pos1[0] + dx, pos1[1] + dy), (pos2[0] + dx, pos2[1] + dy)
                if 0 <= nxt1[0] < N and 0 <= nxt1[1] < N and 0 <= nxt2[0] < N and 0 <= nxt2[1] < N:
                    if board[nxt1[0]][nxt1[1]] == 0 and board[nxt2[0]][nxt2[1]] == 0 and (nxt1, nxt2) not in visited:
                        queue.append(((nxt1, nxt2), time + 1))
                        visited.add((nxt1, nxt2))
            #2️⃣ 회전 이동
            for nxt in get_rotations((pos1, pos2)):
                if nxt not in visited:
                    queue.append((nxt, time + 1))
                    visited.add(nxt)
    return bfs()