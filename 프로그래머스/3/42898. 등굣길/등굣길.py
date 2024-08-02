def solution(m, n, puddles):
    p=[[0]*(m+1) for _ in range(n+1)] #격자 이동 위치 정보 초기화
    p[1][1]=1 #집 초기화
    for y in range(1,n+1):
        for x in range(1,m+1):
            if [x,y] in puddles: #침범구역이면 다음으로 넘기기
                continue
            b1=p[y-1][x] #우측이동
            b2=p[y][x-1] #좌측이동
            if [x,y-1] in puddles: #장애물일 경우
                b1=0
            if [x-1,y] in puddles: #장애물일 경우
                b2=0
            p[y][x]+=b1+b2 #기존 경로에 이동 경로 수 더하기
    answer=p[n][m]%1000000007
    return answer