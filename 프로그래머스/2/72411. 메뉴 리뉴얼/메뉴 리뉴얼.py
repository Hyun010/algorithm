from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    for c in course:
        count = defaultdict(int) #속도를 위한 딕셔너리
        for order in orders:
            for comb in combinations(sorted(order), c): #c개의 단품 조합
                count[comb] += 1#조합 출현 빈도
        max_count = 0
        for cnt in count.values(): #최대출현빈도
            if cnt > max_count:
                max_count = cnt
        for menu, cnt in count.items():
            if cnt == max_count and cnt > 1: #가장 많이 주문된 조합(2명 이상)
                answer.append(''.join(menu))
    return sorted(answer) #사전순 정렬
