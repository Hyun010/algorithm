def solution(lines):
    answer = 0
    lines.sort(key=lambda x: x[0]) #스타트 기준으로 오름 차순 정렬로 맞춰두기
    cs,ce=lines[0] #처음 시작과 끝
    for l in lines[1:]: #나머지 계산
        s,e=l # 새로운 처음과 끝
        if ce<=s: #기준이 바뀜
            cs,ce=s,e
            continue #새로운 선 불러오기
        maxs, mine,maxe=max(cs,s),min(ce,e),max(ce,e) #처음과 새로운 시작중 큰 값, 끝점의 최소와 최대
        answer+=abs(mine-maxs) #길이 더하기
        cs,ce=mine,maxe #새로운 선 불러오기
    return answer