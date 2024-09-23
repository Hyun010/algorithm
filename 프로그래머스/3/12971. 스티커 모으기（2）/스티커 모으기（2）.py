def solution(sticker):
    if len(sticker) == 1: #스티커의 개수가 1개인 경우 예외처리
        return sticker[0]
    #스티커 배열을 두 가지 경우로 나누어 처리
    #1. 1포함(마지막X)
    #2. 1X(마지막 포함)
    def max_sticker_sum(stickers):
        n = len(stickers)
        if n == 1: #예외처리
            return stickers[0]
        dp = [0] * n #dp 배열 초기화
        dp[0] = stickers[0] #첫 번째 스티커 선택
        dp[1] = max(stickers[0], stickers[1]) #1,2 중 큰 것 선택
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + stickers[i]) #선택 여부에 따라 최대값 계산
        return dp[-1] #최대값
    return max(max_sticker_sum(sticker[:-1]), max_sticker_sum(sticker[1:])) #0에서 시작, 1에서 시작