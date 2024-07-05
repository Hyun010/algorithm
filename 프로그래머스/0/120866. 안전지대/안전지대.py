def solution(board):
    answer = 0
    n=len(board) #보드의 크기
    for x,row in enumerate(board): #행 x
        for y,area in enumerate(row): #열 y
            if area==1: #지뢰면
                for dx in [-1,0,1]: #좌우 대각선
                    for dy in [-1,0,1]: #상하 대각선
                        nx=x+dx #좌표 조정
                        ny=y+dy #좌표 조정
                        
                        if 0<=ny<n and 0<=nx<n and board[nx][ny]!=1: #경계면 조건 보드 내에 있고 지뢰간 아니라면 X표시(위험)
                            board[nx][ny]="X"
    answer=sum([area.count(0) for area in board]) #보드에서 안전지대인 0의 개수
    return answer