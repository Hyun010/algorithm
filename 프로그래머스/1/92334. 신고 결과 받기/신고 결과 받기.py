def solution(id_list, report, k):
    #신고당한 카운트
    report_count = {user: 0 for user in id_list}
    #신고한 유저 담는 set 딕셔너리
    reported_by = {user: set() for user in id_list}
    for r in report:
        reporter, reported = r.split() #신고한, 당한 유저 파싱
        if reported not in reported_by[reporter]:
            reported_by[reporter].add(reported) #중복 신고 방지
            report_count[reported] += 1 #신고당한 횟수 증가
    #k번 이상 신고된 유저를 찾음
    suspended_users = {user for user, count in report_count.items() if count >= k}
    answer = [0] * len(id_list)
    for i, user in enumerate(id_list):
        for reported in reported_by[user]:
            if reported in suspended_users:
                answer[i] += 1 #정지된 유저를 신고한 경우 메일 수 증가
    return answer