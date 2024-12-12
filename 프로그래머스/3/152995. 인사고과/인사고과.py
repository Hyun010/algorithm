def solution(scores):
    wanho = scores[0] #본인
    wanho_sum = sum(wanho) #본인 점수 합
    scores.sort(key=lambda s: (-s[0], s[1])) #내림차순, 오름차순 정렬
    max_company, answer = 0, 1 #최대, 등수
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]: #두개다 작은 경우
            return -1 #인센X
        if max_company <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1 #등수 밀림
            max_company = s[1]
    return answer