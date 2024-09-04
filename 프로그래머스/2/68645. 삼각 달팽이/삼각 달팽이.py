def solution(n):
    # 삼각형을 저장할 리스트 초기화
    triangle = [[0] * i for i in range(1, n + 1)]
    # 현재 위치와 숫자 초기화
    x, y = -1, 0
    num = 1
    # 주어진 크기 n만큼 반복
    for i in range(n):
        # 방향에 따라 반복 횟수를 줄여가면서 진행
        for _ in range(i, n):
            # 이동 방향에 따라 좌표를 설정
            if i % 3 == 0:  # 아래로 이동
                x += 1
            elif i % 3 == 1:  # 오른쪽으로 이동
                y += 1
            else:  # 대각선 위로 이동
                x -= 1
                y -= 1

            # 현재 위치에 숫자 배치
            triangle[x][y] = num
            num += 1

    # 결과를 담을 리스트 초기화
    answer = []
    
    # 삼각형을 순서대로 한 줄로 변환
    for row in triangle:
        answer.extend(row)

    # 결과 반환
    return answer