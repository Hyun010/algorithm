def solution(stones, k):
    #건널 수 있는지 확인하는 함수
    def can_cross(mid):
        skip = 0 #건너뛴 디딤돌 수
        for stone in stones:
            if stone - mid < 0: #건너뛰기 가능
                skip += 1 #추가
                if skip >= k: #건너뛴 수 k한계이상
                    return False #끝
            else:
                skip = 0 #디딤돌 밟아서 초기화
        return True #계속 가능
    
    left, right = 1, max(stones) #1명 최대 명수로 초기화(이진탐색을 위해)
    while left <= right: #탈출(왼쪽 포인터가 오른포인터보다 커지면)
        mid = (left + right) // 2 #중앙값
        if can_cross(mid): #건너뛰기 가능한가
            left = mid + 1 #성공해서 다음 수 부터 다시 확인
        else: #실패해서 낮춰서 시도
            right = mid - 1
    return right