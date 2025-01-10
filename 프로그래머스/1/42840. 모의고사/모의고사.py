def solution(answers):
    answer = []
    #맞힌 개수 초기화
    count1 = 0
    count2 = 0
    count3 = 0
    #학생들 답
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    
    #받은 답과 각 학생들의 답을 비교하기 위해 + 반복을 위해 나머지 사용
    for idx, a in enumerate(answers):
        if(ans1[idx%len(ans1)] == a): # idx문제수 %계속 반복해서 사용
            count1 += 1

    for idx, a in enumerate(answers):
        if(ans2[idx%len(ans2)] == a):
            count2 += 1

    for idx, a in enumerate(answers):
        if(ans3[idx%len(ans3)] == a):
            count3 += 1

    #최고로 많이 맞힌 개수
    maxcount = max([count1, count2, count3])
    
    #최고값만 등장 시키기
    if(count1 == maxcount):
        answer.append(1)
    if(count2 == maxcount):
        answer.append(2)
    if(count3 == maxcount):
        answer.append(3)

    answer.sort() #오름차순 정렬 이뻐보이기
    return answer