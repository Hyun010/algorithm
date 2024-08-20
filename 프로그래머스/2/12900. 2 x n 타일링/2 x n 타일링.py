def solution(n):
    # 경우의 수를 저장할 배열 초기화
    dp = [0] * (n + 1)
    dp[0] = 1  # n이 0일 때, 한 가지 방법 (아무것도 놓지 않음)
    if n >= 1:
        dp[1] = 1  # n이 1일 때, 한 가지 방법 (세로로 놓기)
    for i in range(2, n + 1):
        #i-1 길이에 세로로 타일을 놓는 경우, i-2 길이에 가로로 타일을 놓는 경우
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007 
    return dp[n]  # n 길이를 채우는 경우의 수 반환