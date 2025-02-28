def solution(matrix_sizes):
    n = len(matrix_sizes) #행렬의 개수
    #dp[i][j]는 i부터 j까지의 행렬을 곱할 때 필요한 최소 곱셈 횟수
    dp = [[0] * n for _ in range(n)]
    #행렬 곱셈의 순서에 따라 연산 횟수를 계산
    for length in range(2, n + 1): #곱할 행렬의 개수
        for i in range(n - length + 1): #시작 인덱스
            j = i + length - 1 #끝 인덱스
            dp[i][j] = float('inf') #초기값을 무한대로 설정
            # i부터 j까지의 행렬을 곱하는 경우를 고려
            for k in range(i, j): #분할 지점
                #곱셈 횟수 계산: dp[i][k] + dp[k + 1][j] + 곱셈 연산 횟수
                q = dp[i][k] + dp[k + 1][j] + matrix_sizes[i][0] * matrix_sizes[k + 1][0] * matrix_sizes[j][1]
                if q < dp[i][j]:
                    dp[i][j] = q #최소값으로 업데이트

    return dp[0][n - 1] #전체 행렬을 곱할 때의 최소 곱셈 횟수 반환