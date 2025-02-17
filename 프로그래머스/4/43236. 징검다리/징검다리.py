def solution(distance, rocks, n):
    #바위 정렬
    rocks.sort()
    rocks.append(distance)
    #이분 탐색 초기 설정
    left, right = 0, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2 #최소 거리의 후보
        #바위 제거
        prev = 0 #시작점(0)부터 시작
        removed = 0 #제거한 바위 개수
        for rock in rocks:
            if rock - prev < mid: #거리가 mid보다 작으면 제거
                removed += 1
                if removed > n: #제거 가능 개수 초과 시 중단
                    break
            else:
                prev = rock #유지하는 경우, 이전 위치 갱신
        #제거 개수에 따라 이분 탐색 범위 조정
        if removed > n: #제거한 바위가 너무 많으면 mid 감소
            right = mid - 1
        else: #가능한 경우 mid 증가
            answer = mid
            left = mid + 1
    return answer