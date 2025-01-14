def solution(line):
    points = [] #교점
    n = len(line) #직선 개수
    for i in range(n): #교점을 계산
        for j in range(i + 1, n):
            A1, B1, C1 = line[i]
            A2, B2, C2 = line[j]
            #두 직선의 교점 계산을 위한 변수
            det = A1 * B2 - A2 * B1
            
            #두 직선이 평행하지 않은 경우
            if det != 0:
                #교점 (x, y) 계산
                x = (B1 * C2 - B2 * C1) / det
                y = (A2 * C1 - A1 * C2) / det
                #정수 좌표인 경우에만 저장
                if x.is_integer() and y.is_integer():
                    points.append((int(x), int(y)))
    #교점의 최소/최대 x, y 좌표 계산
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)

    #결과를 저장할 격자판 초기화
    grid = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    #별을 그릴 위치에 '*' 표시
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'
    return [''.join(row) for row in grid]