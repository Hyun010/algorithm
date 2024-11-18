def solution(n, t, m, timetable):
    #크루 오름차순으로 정렬(분)
    timetable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    shuttle_time = 540 #셔틀 시작시간(분)
    for i in range(n):
        #현재 가능 크루목록
        available_crew = [time for time in timetable if time <= shuttle_time]
        if i == n - 1: #마지막 셔틀인 경우
            if len(available_crew) < m: #수용인원 보다 적으면 셔틀 시간 맞춰 오기
                last_arrival = shuttle_time
            else: #수용인원보다 많으면 마지막 사람보다 1분 일찍 오기
                last_arrival = available_crew[m - 1] - 1
            break
        else:
            timetable = timetable[min(m, len(available_crew)):] #제거한 목록
            shuttle_time += t #다음셔틀
    answer=f"{last_arrival // 60:02}:{last_arrival % 60:02}"
    return answer