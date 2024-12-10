#분으로 변경함수
def time_to_minutes(t):
    hh, mm = map(int, t.split(':'))
    return hh * 60 + mm

def solution(plans):
    answer = []
    ongoing_tasks = [] #진행 목록 스택
    current_time = 0 #현재 시간
    #시각을 분으로 변경
    plans = [[name, time_to_minutes(start), int(playtime)] for name, start, playtime in plans]
    #시작 시각 기준 정렬
    plans.sort(key=lambda x: x[1])
    for name, start, playtime in plans:
        #현재보다 시작시간 빠른->진행중 과제 처리
        while ongoing_tasks and current_time < start:
            last_task_name, remaining_time = ongoing_tasks.pop()
            finish_time = current_time + remaining_time #끝나는 시각
            #현재 시간 업데이트
            if finish_time <= start:
                #과제컷->결과 추가
                answer.append(last_task_name)
                current_time = finish_time
            else:
                #과제컷X->남은 시간을 스택 추가
                ongoing_tasks.append((last_task_name, remaining_time - (start - current_time)))
                current_time = start
                break
        #새로운 과제 시작
        ongoing_tasks.append((name, playtime))
        current_time = start
    #남아있는 과제 처리
    while ongoing_tasks:
        last_task_name, remaining_time = ongoing_tasks.pop()
        answer.append(last_task_name)
    return answer