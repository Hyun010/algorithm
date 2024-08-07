def solution(n, lost, reserve):
    s=set(lost)&set(reserve) #잃어버린 사람중 여벌 있는분
    lost=sorted(list(filter(lambda x: x not in s,lost))) #잃어버린분 작은순부터 s겹치는 것 제거
    reserve=sorted(list(filter(lambda x: x not in s,reserve))) #여벌 남은 사람 작은순부터 s 겹치는 것 제거
    for i in lost: #잃어버린 사람 돌기
        if (i-1) in reserve: #전사람
            reserve.remove(i-1) #여벌 제거
        elif (i+1) in reserve: #뒷사람
            reserve.remove(i+1) #여벌 제거
        else: #제거 못해서 한명 못참여
            n-=1
    return n