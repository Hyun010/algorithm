def solution(n, tops):
    MOD = 10007 #문제에서 주어진 모듈러 값
    t = 2 * n + 1 #전체 타일 개수 (2n + 1)
    dp = [0] * (t + 1) #DP 테이블 초기화
    dp[0] = 1 #첫 번째 경우의 수
    dp[1] = 1 #두 번째 경우의 수
    for i in range(2, t + 1):
        if i % 2 == 0 and tops[(i - 1) // 2] == 1: #산 모양일 경우
            dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % MOD
        else: #일반적인 경우
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    return dp[t]