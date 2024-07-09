def solution(n, works):
    answer = 0
    if sum(works) <=n: #시간 내에 완성할 경우 피로도 0
        return 0
    works.sort(reverse = True) #최소화를 위한 조건 내림차순 정렬(시간효율)
    for i in range(n):
        m=max(works) #최댓값을 활용하여 탈출 조건 만들기
        j=0 #인덱스
        while(1):
            if works[j] !=m: #탈출 조건(최소화를 위해 최댓값과 비교 후 같지 않으면 탈출)
                break
            works[j]-=1 #일 작업량 1
            n-=1 #일한 시간 1
            j+=1 #다음 작업 인덱스 이동
            if n==0: #퇴근 시간
                break
        if n==0: #퇴근시간
            break
    for w in works: #피로도 계산
        answer+=w**2
    return answer