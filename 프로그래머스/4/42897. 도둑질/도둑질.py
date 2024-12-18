def solution(money):
    n = len(money)
    #첫 집을 털 경우
    def rob_first_house():
        dp = [0] * (n - 1) #첫 집을 털 경우, 마지막 집은 털 수 없음
        dp[0] = money[0]
        dp[1] = max(money[0], money[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
        return dp[n - 2]
    #첫 집을 털지 않는 경우
    def rob_without_first_house():
        dp = [0] * n
        dp[1] = money[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
        return dp[n - 1]
    return max(rob_first_house(), rob_without_first_house())