#시간을 초 변환
def time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s

#초->HH:MM:SS로 변환
def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def solution(play_time, adv_time, logs):
    #시간->초 변환
    play_time_seconds = time_to_seconds(play_time) #동영상 시간
    adv_time_seconds = time_to_seconds(adv_time) #광고 시간
    #재생기록 초로 변환->시작,끝 저장
    viewer_logs = []
    for log in logs:
        start, end = log.split('-')
        viewer_logs.append((time_to_seconds(start), time_to_seconds(end)))
    #누적 재생시간
    time_slots = [0] * (play_time_seconds + 1)
    #각 시청자의 재생 구간에 대해 누적 재생시간을 기록
    for start, end in viewer_logs:
        time_slots[start] += 1
        time_slots[end] -= 1
    #누적 재생시간 계산
    for i in range(1, play_time_seconds + 1):
        time_slots[i] += time_slots[i - 1]
    #광고 구간의 누적 재생시간을 계산
    current_sum = sum(time_slots[:adv_time_seconds])
    max_sum = current_sum
    max_start_time = 0
    for start in range(1, play_time_seconds - adv_time_seconds + 1):
        current_sum += time_slots[start + adv_time_seconds - 1] - time_slots[start - 1]
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_time = start
    return seconds_to_time(max_start_time)