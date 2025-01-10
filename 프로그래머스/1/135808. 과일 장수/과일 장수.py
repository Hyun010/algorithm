def solution(k, m, score):
    answer = 0
    s=[]
    score.sort()
    while True:
        if len(s)==m:
            answer+=min(s)*m
            s=[]
        if len(score)==0:
            return answer
        s.append(score[-1])
        score.pop()