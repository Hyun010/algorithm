def solution(a):
    #왼쪽에서 최소값
    left_min = [float('inf')] * len(a)
    min_so_far = float('inf')
    for i in range(len(a)):
        min_so_far = min(min_so_far, a[i])
        left_min[i] = min_so_far
    #오른쪽에서 최소값
    right_min = [float('inf')] * len(a)
    min_so_far = float('inf')
    for i in range(len(a) - 1, -1, -1):
        min_so_far = min(min_so_far, a[i])
        right_min[i] = min_so_far
    answer = 0
    for i in range(len(a)):
        #왼쪽 최소값, 오른쪽 최소값보다 작거나 같으면 최후
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
    return answer