def solution(board):
    if not board or not board[0]:  # 빈 보드인 경우
        return 0

    rows = len(board)  # 보드의 행 수
    cols = len(board[0])  # 보드의 열 수
    max_square_length = 0  # 가장 큰 정사각형의 변 길이 초기화

    # DP 테이블 생성 (보드 크기와 동일)
    dp = [[0] * cols for _ in range(rows)]

    # 보드의 각 칸을 순회
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:  # 현재 칸이 1인 경우
                if i == 0 or j == 0:  # 첫 번째 행이나 열인 경우
                    dp[i][j] = 1  # 1x1 정사각형으로 초기화
                else:
                    # 왼쪽, 위쪽, 대각선 위쪽 왼쪽의 최소값 + 1
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
                # 최대 정사각형 변 길이 갱신
                max_square_length = max(max_square_length, dp[i][j])

    # 최대 정사각형의 넓이를 반환
    return max_square_length * max_square_length