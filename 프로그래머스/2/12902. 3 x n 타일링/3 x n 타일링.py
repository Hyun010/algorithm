def solution(n):
    MOD = 1_000_000_007
    if n % 2 != 0:
        return 0 #n이 홀수인 경우는 채울 수 없음
    dp = [0] * (n + 1)
    dp[0] = 1 #초기값 설정
    dp[2] = 3 #초기값 설정
    for i in range(4, n + 1, 2):
        dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % MOD
    return dp[n]