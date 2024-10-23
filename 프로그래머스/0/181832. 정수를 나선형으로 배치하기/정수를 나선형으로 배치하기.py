def solution(n):
    answer = [[0] * n for _ in range(n)] #초기화(2차원 배열)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] #방향 : 우, 하, 좌, 상(시계)
    dir_index = 0 #현재 방향인덱스
    row, col = 0, 0 #시작위치
    for num in range(1, n * n + 1):
        answer[row][col] = num #현재위치 숫자배치
        #다음 위치계산
        next_row = row + directions[dir_index][0]
        next_col = col + directions[dir_index][1]
        #다음 위치 배열범위 밖이거나 이미 수 배치->방향 전환
        if (0 <= next_row < n and 0 <= next_col < n and answer[next_row][next_col] == 0):
            row, col = next_row, next_col #다음위치 이동
        else: #방향 전환 
            dir_index = (dir_index + 1) % 4 #방향인덱스 변경
            row += directions[dir_index][0] 
            col += directions[dir_index][1]
    return answer