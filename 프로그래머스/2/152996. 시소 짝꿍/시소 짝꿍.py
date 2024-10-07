def solution(weights):
    answer = 0
    torque_cnt={}
    #몸무게 빈도 저장
    for w in weights:
        if w in torque_cnt:
            torque_cnt[w]+=1
        else:
            torque_cnt[w]=1
    #2:3, 2:4, 3:4, 1:1(경우의 수)
    ratios=[(2, 3), (2, 4), (3, 4), (1, 1)]
    for w in sorted(torque_cnt):
        for r in ratios:
            target_weight=w*r[1]/r[0] #ratio[0]:ratio[1] 비율을 만족하는 짝
            if target_weight.is_integer() and int(target_weight) in torque_cnt:
                #짝이 같은 몸무게
                if r == (1, 1):
                    answer += torque_cnt[w] * (torque_cnt[w] - 1) // 2
                else:
                    #다른 몸무게와 짝
                    answer += torque_cnt[w] * torque_cnt[int(target_weight)]
        #이미 탐색한 몸무게는 중복 카운팅을 방지-> 제거
        torque_cnt.pop(w)
    return answer