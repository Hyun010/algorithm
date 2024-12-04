def solution(board, skill):
    N = len(board) #행의 수
    M = len(board[0]) #열의 수
    answer = 0
    damage = [[0] * (M + 1) for _ in range(N + 1)] #내구도 변화 배열
    for s in skill: #누적합 셋팅
        type, r1, c1, r2, c2, degree = s
        if type == 1: #적의 공격
            damage[r1][c1] -= degree
            damage[r1][c2 + 1] += degree
            damage[r2 + 1][c1] += degree
            damage[r2 + 1][c2 + 1] -= degree
        elif type == 2: #아군의 회복
            damage[r1][c1] += degree
            damage[r1][c2 + 1] -= degree
            damage[r2 + 1][c1] -= degree
            damage[r2 + 1][c2 + 1] += degree
    for i in range(N):
        for j in range(M):
            #누적 합
            if i > 0:
                damage[i][j] += damage[i - 1][j]
            if j > 0:
                damage[i][j] += damage[i][j - 1]
            if i > 0 and j > 0:
                damage[i][j] -= damage[i - 1][j - 1]
            final_health = board[i][j] + damage[i][j] #최종 보드결과 저장
            if final_health > 0: #1이상->파괴X
                answer += 1
    return answer  # 결과 반환