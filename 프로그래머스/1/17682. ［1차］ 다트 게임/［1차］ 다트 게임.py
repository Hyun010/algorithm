def solution(dartResult):
    answer = 0
    jegop={"S":1,"D":2,"T":3} #보너스 초기화
    score=[] #점수 저장 공간
    t="" #다트판 숫자 임시 저장
    for c in dartResult:
        if c.isdigit(): #숫자면 임시로 쌓아두기
            t+=c
        elif c.isalpha(): #보너스면 제곱한 점수 등록하고 임시저장 초기화
            score.append((int(t)**jegop[c]))
            t=""
        elif c=="*":
            if len(score)>1: #이전 점수가 존재할 때 옵션 적용 이전 점수와 현재 점수 2배
                score[-2]*=2
            score[-1]*=2 #이전 점수 없을 때는 현재 점수만 2배
        elif c=="#":
            score[-1]*=-1 #현재 점수 -적용 옵션
    answer=sum(score) #점수 합계
    return answer