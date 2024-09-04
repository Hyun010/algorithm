def solution(hp):
    answer = 0
    answer=answer+(hp//5)
    hp%=5
    answer=answer+(hp//3)
    hp%=3
    answer=answer+(hp//1)
    return answer