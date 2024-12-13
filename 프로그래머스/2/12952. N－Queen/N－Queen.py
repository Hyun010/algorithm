def solution(n):
    #열과 대각선의 사용 여부를 저장할 배열
    cols = [0] * n #열 사용 여부
    diag1 = [0] * (2 * n - 1) #왼쪽 대각선 (row + col)
    diag2 = [0] * (2 * n - 1) #오른쪽 대각선 (row - col + (n - 1))
    result = 0 #가능한 배치 수를 저장할 변수

    def n_queens(row):
        nonlocal result
        if row == n: #모든 퀸을 배치했을 경우
            result += 1
            return

        for col in range(n):
            if cols[col] or diag1[row + col] or diag2[row - col + (n - 1)]:
                continue #사용 중인 열이나 대각선이면 건너뜀

            #퀸을 배치
            cols[col] = 1
            diag1[row + col] = 1
            diag2[row - col + (n - 1)] = 1

            n_queens(row + 1) #다음 행으로 이동

            #퀸을 제거
            cols[col] = 0
            diag1[row + col] = 0
            diag2[row - col + (n - 1)] = 0

    n_queens(0) #첫 row부터 탐색 시작
    return result