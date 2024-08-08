def solution(m, n, board):
    board = [list(row) for row in board] #2차원 배열로 변경, 하나당 확인을 위해
    answer = 0  #지워진 블록의 개수
    while True:
        to_remove = set() #지워야 할 블록의 위치를 저장할 집합
        for i in range(m - 1):  #행을 순회
            for j in range(n - 1):  #열을 순회
                if (board[i][j] != ' ' and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]): # 오른쪽, 아래쪽, 우하쪽 확인결과 같으면
                    to_remove.update([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]) #제거 목록 추가
        if not to_remove: #지울 블럭 없으면 종료
            break
        answer += len(to_remove)  #지워진 블록 개수 증가
        for i, j in to_remove:
            board[i][j] = ' '  #지운 블록 빈 공간 표시
        for j in range(n):
            empty_count = 0  #빈공간 개수
            for i in range(m - 1, -1, -1):  #아래에서 위로 확인
                if board[i][j] == ' ':
                    empty_count += 1  #빈 공간 개수 증가
                elif empty_count > 0: #빈 공간이 있으면
                    board[i + empty_count][j] = board[i][j] #빈공간 채우기
                    board[i][j] = ' '  #원래 위치 빈공간으로 표시
    return answer  # 최종적으로 지워진 블록의 개수를 반환