def solution(alp, cop, problems):
    #문제를 풀기 위해 필요한 최대 알고력과 코딩력을 계산
    max_alp = max(alp, max(p[0] for p in problems))
    max_cop = max(cop, max(p[1] for p in problems))
    #DP 테이블 초기화
    dp = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0 #초기 상태의 시간은 0

    #DP 테이블을 채우기
    for a in range(max_alp + 1):
        for c in range(max_cop + 1):
            if dp[a][c] == float('inf'):
                continue
            #알고력과 코딩력을 각각 1씩 증가시키는 경우
            if a + 1 <= max_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            if c + 1 <= max_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            #각 문제를 풀 수 있는지 확인
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    new_alp = min(max_alp, a + alp_rwd)
                    new_cop = min(max_cop, c + cop_rwd)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[a][c] + cost)
    #모든 문제를 풀기 위해 필요한 최소 시간을 반환
    return dp[max_alp][max_cop]