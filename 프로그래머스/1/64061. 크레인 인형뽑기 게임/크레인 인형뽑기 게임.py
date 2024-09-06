def solution(board, moves):
    answer = 0
    basket = []

    # moves 배열을 순회합니다.
    for move in moves:
        # 크레인이 선택한 열의 인덱스를 0부터 시작하는 인덱스로 변환합니다.
        column = move - 1
        
        # 해당 열에서 인형을 찾기 위해 아래에서 위로 탐색합니다.
        for row in range(len(board)):
            # 현재 위치에 인형이 있는 경우
            if board[row][column] != 0:
                # 인형을 바구니에 추가합니다.
                current_doll = board[row][column]
                basket.append(current_doll)
                
                # 인형을 집은 후 해당 위치를 빈 공간(0)으로 만듭니다.
                board[row][column] = 0
                
                # 바구니의 가장 위 인형이 이전 인형과 같은지 확인합니다.
                if len(basket) >= 2 and basket[-1] == basket[-2]:
                    # 같은 인형이 두 개 연속으로 쌓이면 제거합니다.
                    basket.pop()  # 가장 위 인형 제거
                    basket.pop()  # 그 아래 인형도 제거
                    answer += 2  # 터뜨려진 인형 개수 증가
                break  # 인형을 찾았으므로 다음 move로 넘어갑니다

    return answer  # 최종적으로 터뜨려진 인형의 개수를 반환합니다.