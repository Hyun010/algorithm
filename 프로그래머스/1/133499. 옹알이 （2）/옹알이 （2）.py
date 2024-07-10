def solution(babbling):
    answer = 0
    ok=['aya','ye','woo','ma'] #기본 단어 4개
    for i in babbling:
        if i in ok: #기본 단어면
            answer+=1
        else: #합성어일 경우
            s1='' #단어 저장
            s2='' #연속단어 검사 단어저장
            for j in i:
                s1+=j #단어 저장중
                if s1!=s2 and s1 in ok: #연속이 아니며 들어있다면
                    s2=s1 #연속단어 검사 단어저장
                    s1='' #초기화
            if s1=='': #기본단어로된 합성어면
                answer+=1
    return answer
