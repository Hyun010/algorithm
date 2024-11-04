def solution(n, times):
    left = 1
    right = min(times) * n #최대 시간 초기값은 낮은 시간 n명 다했을 때
    while left <= right:
        mid = (left + right) // 2 #중간값
        total_people = sum(mid // time for time in times) #mid 시간 내 총 명수
        if total_people < n: #적으면 left를 mid위로
            left = mid + 1
        else: #많으면 right를 mid아래로
            right = mid - 1      
    return left