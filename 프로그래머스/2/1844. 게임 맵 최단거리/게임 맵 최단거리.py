from collections import deque

def solution(maps):
    n=len(maps) #행의 길이
    m=len(maps[0]) #열의 길이
    visited=[[0]*m for i in range(n)] #방문 체크
    dy=[0,1,0,-1] #좌하우상 확인
    dx=[-1,0,1,0] #좌하우상 확인
    q=deque([(0,0)]) #큐 초기화
    visited[0][0]=1 #캐릭터 위치
    while q: #도착까지 무한 루프
        x,y=q.popleft() #기존 좌표
        for i in range(4): #상하좌우 이동
            nx,ny=x+dx[i],y+dy[i] #상하좌우 이동 좌표
            if 0<=nx<n and 0<=ny<m: #보드판 안에 존재하면
                if visited[nx][ny]==0 and maps[nx][ny]==1: #방문하지 않고 이동가능한 1이라면
                    visited[nx][ny]=visited[x][y]+1 #이동경로 숫자추가
                    q.append((nx,ny)) #다음 이동좌표 추가
    if visited[n-1][m-1]==0: #방문 X
        return -1
    else:
        return visited[n-1][m-1]