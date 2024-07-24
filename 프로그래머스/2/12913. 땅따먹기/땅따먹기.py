def solution(land):
    N = len(land)
    dp = [[0] * 4 for _ in range(N)] #합계 최대 초기화
    for j in range(4): #1행 초기화
        dp[0][j] = land[0][j]
    for i in range(1, N): #행
        for j in range(4): #열
            #land 값에 이전값 곂치지 않는 것중 제일 큰것으로 입력
            dp[i][j] = land[i][j] + max(dp[i-1][(j+1)%4], dp[i-1][(j+2)%4], dp[i-1][(j+3)%4]) 
    return max(dp[N-1]) #처음이 제일 큰값