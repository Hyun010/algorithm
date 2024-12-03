def solution(n, money):
    MOD = 1000000007 #나눔수
    dp = [0] * (n + 1) #dp 초기화, i원 거스름 방법 수
    dp[0] = 1 #0원은 1가지
    for coin in money:
        #화폐 단위로 거스름 방법 업데이트
        for amount in range(coin, n + 1):
            dp[amount] = (dp[amount] + dp[amount - coin]) % MOD
    return dp[n]