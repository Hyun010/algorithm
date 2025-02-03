from collections import deque, defaultdict

def solution(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * cols for _ in range(rows)] #방문 여부 저장
    oil_clusters = defaultdict(list) #{가로(열) 번호: [덩어리 크기 리스트]}
    def bfs(start_x, start_y):
        """BFS로 석유 덩어리 탐색 후, 해당 열 번호에 저장"""
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True
        count = 1 #현재 덩어리 크기
        positions = [(start_x, start_y)] #덩어리 위치 저장
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    positions.append((nx, ny))
                    count += 1
        #가로(열) 번호에 따라 저장
        affected_columns = set(y for _, y in positions) #덩어리가 속한 열 모음
        for col in affected_columns:
            oil_clusters[col].append(count)
    #모든 1을 탐색하여 BFS 실행 (O(NM))
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j) #BFS 실행하여 덩어리 크기 저장
    #각 가로 번호(열) 별로 덩어리 크기 합산 후 최댓값 계산 (O(M))
    max_oil = max(sum(cluster) for cluster in oil_clusters.values())
    return max_oil
