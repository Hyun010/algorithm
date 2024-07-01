def solution(N, stages):
    per_stages={} #딕셔너리 스테이지별 실패율
    all_players=len(stages) #전체 플레이어
    for i in range(1,N+1):
        if all_players!=0:
            fail_players=stages.count(i) #스테이지별 실패한 사람 수
            per_stages[i]=fail_players/all_players #실패율
            all_players-=fail_players #스테이지 도달 사람
        else:
            per_stages[i]=0
    answer=sorted(per_stages,key=lambda x:per_stages[x],reverse=True) #내림차순 정렬
    return answer