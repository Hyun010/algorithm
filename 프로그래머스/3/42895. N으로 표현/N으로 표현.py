def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    #사칙연산을 통해 새로운 수를 생성
                    dp[i].add(a + b) #덧셈
                    dp[i].add(a - b) #뺄셈
                    dp[i].add(a * b) #곱셈
                    if b != 0: #0으로 나누는 경우를 피함
                        dp[i].add(a // b) #나눗셈
        if number in dp[i]:
            return i #number를 표현할 수 있는 최소 횟수
    return -1