def solution(triangle):
    answer = 0
    dp=[[0 for i in range(len(triangle))] for i in range(len(triangle))]
    dp[0][0]=triangle[0][0]
    for i in range(1,len(triangle)):
        n=len(triangle[i])
        for j in range(n):
            if i==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            else:
                dp[i][j]=max(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
    answer=max(dp[len(triangle)-1])
    return answer