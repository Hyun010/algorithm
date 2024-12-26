def solution(name, yearning, photo):
    answer = []
    t=0
    for p in photo:
        for idx,n in enumerate(name):
            if n in p:
                t+=yearning[idx]
        answer.append(t)
        t=0
    return answer