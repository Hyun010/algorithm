def solution(k, score):
    answer = []
    s=[]
    for idx,i in enumerate(score):
        if idx<k:
            s.append(i)
            s.sort(reverse=True)
            answer.append(s[-1])
        else:
            if s[-1]<=i:
                s.pop()
                s.append(i)
                s.sort(reverse=True)
                answer.append(s[-1])
            else:
                answer.append(s[-1])
    return answer