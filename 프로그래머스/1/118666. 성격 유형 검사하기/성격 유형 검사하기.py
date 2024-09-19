def solution(survey, choices):
    answer = []
    score_map = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0} #스코어 초기화
    for i in range(len(survey)):
        s = survey[i] #질문 성격 유형
        c = choices[i] #선택지
        if c < 4: #비동의
            score = 4 - c #매우 비동의 3, 비동의 2, 약간 비동의 1
            score_map[s[0]] += score  #비동의시 첫 점수 증가
        elif c > 4: # 동의 관련 선택지
            score = c - 4 #약간 동의 1, 동의 2, 매우 동의 3
            score_map[s[1]] += score #동의시 둘째 점수 증가
    
    for key in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if score_map[key[0]] > score_map[key[1]]:
            answer.append(key[0]) #처음이 큼
        elif score_map[key[0]] < score_map[key[1]]:
            answer.append(key[1]) #두번째가 큼
        else:
            # 같을 시 사전순 증가(둘 중 작은 수)
            answer.append(min(key))
    answer=''.join(answer)
    return answer