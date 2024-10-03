def solution(maps):
    rows = len(maps) #세로
    cols = len(maps[0]) #가로
    visited = [[False] * cols for _ in range(rows)] #방문여부
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] #상하좌우 방향
    
    def dfs(x, y):
        stack = [(x, y)] #시작
        visited[x][y] = True #방문
        total_food = int(maps[x][y]) #총식량 현재 식량으로 초기화
        while stack:
            cx, cy = stack.pop() #위치 꺼내기
            for dx, dy in directions: #상하좌우 이동
                nx, ny = cx + dx, cy + dy
                #지도내 방문X 바다가 아닌 경우(식량O)
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True #방문 체크
                    total_food += int(maps[nx][ny]) #합산
                    stack.append((nx, ny)) #이동 후 스택 쌓기
        return total_food
    answer = []
    for i in range(rows):
        for j in range(cols):
            #방문X, 바다X 시작
            if not visited[i][j] and maps[i][j] != 'X':
                days = dfs(i, j) #합산
                answer.append(days) #각 섬 합산 추가
    if not answer: #결과 비면 -1 리턴
        return [-1]
    return sorted(answer) #오름차순 정렬 후 반환
