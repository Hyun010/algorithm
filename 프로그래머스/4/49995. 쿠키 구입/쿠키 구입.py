def solution(cookie):
    n = len(cookie)
    answer = 0
    for m in range(n - 1):
        left_sum = cookie[m]
        right_sum = cookie[m + 1]
        left_index = m
        right_index = m + 1
        while left_index >= 0 and right_index < n:
            if left_sum == right_sum:  
                answer = max(answer, left_sum)
            #더 작은 쪽을 확장
            if left_sum <= right_sum and left_index > 0:
                left_index -= 1
                left_sum += cookie[left_index]
            elif right_sum < left_sum and right_index < n - 1:
                right_index += 1
                right_sum += cookie[right_index]
            else:
                break
    return answer