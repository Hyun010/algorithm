def solution(progresses, speeds):
    answer = []
    while speeds: #작업중
        for i, s in enumerate(speeds): #하루 작업양
            progresses[i]+=s
        cnt=0 #배포 작업 수
        while progresses and progresses[0]>=100: # 작업이 남았고, 100프로이상이면 배포작업(첫작업이 100프로)
            del progresses[0],speeds[0]
            cnt+=1
        if cnt>0:
            answer.append(cnt)
    return answer