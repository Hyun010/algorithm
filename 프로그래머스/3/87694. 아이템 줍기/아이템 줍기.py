from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    #맵 크기를 2배로 확장하여 정확한 경로 판별
    SIZE = 102  # 최대 50이므로 2배(50 * 2 + 여유 공간)
    board = [[0] * SIZE for _ in range(SIZE)]
    #좌표 2배 확장 및 직사각형 테두리 마킹
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 2  # 내부 (이동 불가)
                elif board[i][j] == 0:
                    board[i][j] = 1  # 테두리 (이동 가능)
    #상하좌우 이동
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    #시작점과 도착점도 2배 확장
    start = (characterX * 2, characterY * 2)
    end = (itemX * 2, itemY * 2)
    queue = deque([(start[0], start[1], 0)]) #(x, y, 거리)
    visited = set([start])
    #BFS 실행 (최단 경로 탐색)
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist // 2 #다시 2배 확장한 값 원래 값으로 변환
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < SIZE and 0 <= ny < SIZE and
                (nx, ny) not in visited and board[nx][ny] == 1):
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
