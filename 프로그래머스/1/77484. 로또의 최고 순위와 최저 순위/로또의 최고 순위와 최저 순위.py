def solution(lottos, win_nums):
    ma=0
    mi=0
    scores = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1} #순위 목록
    for l in lottos: #나머지 로또 맞은 갯수 구하기
        if l in win_nums:
            mi+=1
    ma=mi+lottos.count(0) #최소에 가려진 것 다 맞다는 가정하면 최대
    answer=[scores[ma],scores[mi]] #순위 목록 최대, 최소
    return answer