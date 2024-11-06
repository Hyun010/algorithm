def solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = map(int, today.split('.'))
    today_total_days = today_year * 12 * 28 + today_month * 28 + today_day #일 단위 변환
    term_dict = {} #타입:유효기간
    for term in terms:
        type, duration = term.split()
        term_dict[type] = int(duration) * 28 #일 단위 변환
    for i, privacy in enumerate(privacies):
        start_date, term_type = privacy.split()
        start_year, start_month, start_day = map(int, start_date.split('.'))
        start_total_days = start_year * 12 * 28 + start_month * 28 + start_day #일 단위 변환
        if start_total_days + term_dict[term_type] <= today_total_days: #현재날짜가 유효기간 이후면 증가
            answer.append(i + 1)  # i는 0부터 시작하므로 +1
    return answer