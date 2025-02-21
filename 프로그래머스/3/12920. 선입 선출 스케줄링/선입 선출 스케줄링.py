def solution(n, cores):
    if n <= len(cores):
        return n #첫 n개는 코어 개수보다 작거나 같으면 바로 할당 가능
    left, right = 1, max(cores) * n #가능한 시간 범위 설정
    answer_time = right #마지막 작업이 수행되는 시간
    #이진 탐색을 통해 작업이 완료될 최소 시간을 찾음
    while left <= right:
        mid = (left + right) // 2
        total_jobs = sum(mid // core for core in cores) + len(cores)
        if total_jobs >= n:
            answer_time = mid
            right = mid - 1
        else:
            left = mid + 1
    #answer_time-1까지 완료된 작업 수를 계산
    jobs_done = sum((answer_time - 1) // core for core in cores) + len(cores)
    #마지막 작업을 수행하는 코어를 찾기
    for i, core in enumerate(cores):
        if answer_time % core == 0: #현재 시간에 실행되는 코어 확인
            jobs_done += 1
            if jobs_done == n:
                return i + 1  #1-based index이므로 +1