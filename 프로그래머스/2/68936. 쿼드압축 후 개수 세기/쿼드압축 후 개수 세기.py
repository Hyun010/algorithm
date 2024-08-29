def solution(arr):
    # 결과를 저장할 리스트 초기화
    answer = [0, 0]  # [0의 개수, 1의 개수]

    # 주어진 배열을 쿼드압축하는 재귀 함수 정의
    def compress(x, y, size):
        # 현재 영역의 첫 번째 값 저장
        first_value = arr[x][y]
        is_uniform = True  # 현재 영역이 균일한지 여부
        
        # 현재 영역의 모든 값을 확인
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first_value:
                    is_uniform = False  # 균일하지 않으면 False로 설정
                    break
            if not is_uniform:
                break
        
        # 모든 값이 같다면
        if is_uniform:
            answer[first_value] += 1  # 해당 값의 개수 증가
        else:
            # 균일하지 않다면 4개의 정사각형으로 나누어 압축
            new_size = size // 2
            compress(x, y, new_size)          # 왼쪽 위
            compress(x, y + new_size, new_size)  # 오른쪽 위
            compress(x + new_size, y, new_size)  # 왼쪽 아래
            compress(x + new_size, y + new_size, new_size)  # 오른쪽 아래

    # 전체 배열을 압축하기 위해 호출
    compress(0, 0, len(arr))
    
    return answer  # 최종 결과 반환