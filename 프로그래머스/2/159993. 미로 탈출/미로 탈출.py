from collections import deque

def solution(maps):
    #시간, 시작, 레버, 탈출, 미로 크기 초기화
    answer=0
    start = None
    lever = None
    exit = None
    rows, cols = len(maps), len(maps[0])
    #S, L, E 위치 저장
    for r in range(rows):
        for c in range(cols):
            if maps[r][c]=='S':
                start = (r, c)
            elif maps[r][c]=='L':
                lever = (r, c)
            elif maps[r][c]=='E':
                exit = (r, c)
    
    def bfs(start, target):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상하좌우 이동 방향
        queue = deque([start]) #BFS 사용 큐
        visited = [[False] * cols for _ in range(rows)] #방문기록
        visited[start[0]][start[1]] = True #방문 처리
        distance = 0 #시간

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == target: #목표
                    return distance #시간 리턴

                for dx, dy in directions: #이동
                    nx, ny = x + dx, y + dy #이동좌표
                    #범위 내 방문X면 처리
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                        if maps[nx][ny] != 'X': #벽이 아닌 경우
                            visited[nx][ny] = True #방문처리
                            queue.append((nx, ny)) #다음 이동 추가
            distance += 1 #거리추가
        return -1  #목표X->-1 리턴

    distance_to_lever = bfs(start, lever) #시작->레버
    if distance_to_lever == -1:
        return -1 #레버 도달X
    distance_to_exit = bfs(lever, exit) #레버->탈출
    if distance_to_exit == -1:
        return -1 #탈출X

    answer=distance_to_lever + distance_to_exit
    return answer