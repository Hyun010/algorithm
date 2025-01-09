from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    data = defaultdict(list) #조건-점수리스트
    #모든 조합 생성
    for entry in info:
        details = entry.split() #데이터 파싱(빈칸)
        score = int(details[-1]) #점수
        attributes = details[:-1] #점수 제외한 나머지
        #조합 생성(16가지: 각 속성이 "-"인 경우 포함)
        for i in range(16):
            condition = []
            for j in range(4): #4개 속성
                if i & (1 << j): #조건 포함
                    condition.append(attributes[j])
                else: #조건 생략
                    condition.append("-")
            #조건-값
            data[" ".join(condition)].append(score)
    #점수 정렬
    for key in data:
        data[key].sort()
    answer = []
    for q in query:
        q_parts = q.replace(" and ", " ").split() #쿼리 파싱
        condition = " ".join(q_parts[:-1]) #조건
        target_score = int(q_parts[-1]) #조건점수
        if condition in data:
            scores = data[condition]
            #이진 탐색으로 target_score 이상인 점수 개수 찾기
            idx = bisect_left(scores, target_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    return answer
