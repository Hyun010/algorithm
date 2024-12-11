def solution(s):
    answer = []
    index={}
    for i, str in enumerate(s):
        if str not in index:
            answer.append(-1)
        else:
            answer.append(i-index[str])
        index[str]=i
    return answer