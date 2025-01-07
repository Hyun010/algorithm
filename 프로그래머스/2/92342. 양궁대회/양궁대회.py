from copy import deepcopy

def calculate_scores(ryan, apeach):
    ryan_score, apeach_score = 0, 0
    for i in range(11):
        if ryan[i] > apeach[i]:  # 라이언이 더 많이 쏜 경우
            ryan_score += 10 - i
        elif apeach[i] > 0:  # 어피치가 점수를 가져가는 경우
            apeach_score += 10 - i
    return ryan_score, apeach_score

def solution(n, info):
    max_diff = 0 #최대 점수 차이 저장
    answer = [-1] #우승 못할 경우로 초기화
    def dfs(index, arrows_left, ryan):
        nonlocal max_diff, answer
        #종료 조건: 모든 점수를 탐색하거나 화살을 모두 사용한 경우
        if index == 11 or arrows_left == 0:
            ryan_copy = deepcopy(ryan)
            #남은 화살을 마지막 점수(0점)에 추가
            if arrows_left > 0:
                ryan_copy[10] += arrows_left
            #점수 계산
            ryan_score, apeach_score = calculate_scores(ryan_copy, info)
            score_diff = ryan_score - apeach_score

            #최적의 전략 갱신 조건
            if score_diff > max_diff:
                max_diff = score_diff
                answer = ryan_copy
            #점수 차이가 같은 경우 낮은 점수 우선 비교
            elif score_diff == max_diff:
                if ryan_copy[::-1] > answer[::-1]:
                    answer = ryan_copy
            return

        #Case 1: 현재 점수를 포기
        dfs(index + 1, arrows_left, ryan)

        #Case 2: 현재 점수를 얻기 위해 화살 쏘기
        if arrows_left > info[index]:
            ryan[index] = info[index] + 1
            dfs(index + 1, arrows_left - (info[index] + 1), ryan)
            ryan[index] = 0 #백트래킹
    dfs(0, n, [0] * 11)
    if max_diff==0:
        answer=[-1]
    return answer