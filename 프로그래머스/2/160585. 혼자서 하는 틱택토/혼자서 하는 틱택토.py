def solution(board):
    o_count = 0
    x_count = 0
    #게임판 O,X 개수
    for row in board:
        for cell in row:
            if cell == 'O':
                o_count += 1
            elif cell == 'X':
                x_count += 1
    if o_count > x_count + 1:
        return 0
    if x_count > o_count:
        return 0
    #승리 조건을 확인하는 함수
    def check_winner(player):
        #가로, 세로, 대각선 체크
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return True
        #대각선 체크
        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            return True
        return False
    #O와 X의 승리 여부 확인
    o_wins = check_winner('O')
    x_wins = check_winner('X')

    #O가 이겼을 때, O의 개수는 X의 개수보다 1 많아야 함
    if o_wins and o_count != x_count + 1:
        return 0
    #X가 이겼을 때, X의 개수는 O의 개수와 같아야 함
    if x_wins and o_count != x_count:
        return 0
    #두 플레이어가 동시에 이길 수는 없음
    if o_wins and x_wins:
        return 0
    #모든 조건을 통과하면 유효한 게임 상태
    return 1