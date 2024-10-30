import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0]) #요청시점 오름차순 정렬
    current_time = 0 #현재시간
    total_wait_time = 0 #총 대기시간
    completed_jobs = 0 #완료된 작업 수
    job_length = len(jobs) #총 작업 수
    waiting_jobs = [] #대기 중인 작업 리스트
    index = 0 #jobs 인덱스

    while completed_jobs < job_length:
        while index < job_length and jobs[index][0] <= current_time:
            heapq.heappush(waiting_jobs, (jobs[index][1], jobs[index][0]))
            index += 1
        if waiting_jobs:
            # 대기 중인 작업 중에서 가장 소요 시간이 짧은 작업을 선택
            current_job = heapq.heappop(waiting_jobs) #가장 짧은 작업 선택
            start_time = current_time #작업 시작 시간
            current_time += current_job[0] #작업 완료 시간 업데이트
            total_wait_time += (current_time - current_job[1]) #대기 시간 계산
            completed_jobs += 1 #완료된 작업 수 증가
        else:
            #대기 중인 작업이 없으면 시간을 증가시킴
            current_time += 1
    answer=total_wait_time // job_length
    return answer