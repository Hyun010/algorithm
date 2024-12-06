import math

def solution(r1, r2):
    answer = 0
    for x in range(r2 + 1):
        #큰 원 내부 최대 y값(내림)
        max_y = math.floor(math.sqrt(r2**2 - x**2))
        #작은 원 내부 최소 y값(올림, 작은원 조건X->0)
        min_y = math.ceil(math.sqrt(r1**2 - x**2)) if x**2 < r1**2 else 0
        #해당 x->가능한 y값의 개수
        answer += (max_y - min_y + 1)
    return answer * 4 - (r2 - r1 + 1) * 4 #중복 제거
