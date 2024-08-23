def solution(board, h, w):
    # 보드의 크기를 n에 저장
    n = len(board)
    
    # 같은 색으로 색칠된 칸의 개수를 저장할 변수
    count = 0
    # 상하좌우 방향을 나타내는 리스트
    dh = [0, 1, -1, 0]  # 행 변화량
    dw = [1, 0, 0, -1]  # 열 변화량
    
    # 상하좌우 4방향을 체크
    for i in range(4):
        # 체크할 칸의 좌표 계산
        h_check = h + dh[i]
        w_check = w + dw[i]
        
        # 체크할 좌표가 보드 범위 내에 있는지 확인
        if 0 <= h_check < n and 0 <= w_check < n:
            # 같은 색인지 확인
            if board[h][w] == board[h_check][w_check]:
                count += 1  # 같은 색이라면 count 증가

    # 최종 결과 반환
    return count