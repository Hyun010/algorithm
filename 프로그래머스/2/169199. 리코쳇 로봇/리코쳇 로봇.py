from collections import deque

def solution(board):
    start = None #시작
    goal = None #끝
    rows = len(board) #행 크기
    cols = len(board[0]) #열 크기
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] #상하좌우
    
    #시작과 끝 위치 찾기
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                goal = (r, c)
                
    # BFS 초기화
    queue = deque([(start[0], start[1], 0)]) #(행,열,이동횟수)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, moves = queue.popleft()
        if (x, y) == goal: #위치가 목표->이동횟수 리턴
            return moves
        for dx, dy in directions: #상하좌우 이동
            nx, ny = x, y
            #장애물 경계에 닿기까지 이동
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            if (nx, ny) not in visited: #새로운 위치가 방문X
                visited.add((nx, ny)) #방문 체크
                queue.append((nx, ny, moves + 1)) #다음 이동
    return -1 #도달X