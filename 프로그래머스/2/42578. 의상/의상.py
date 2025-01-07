def solution(clothes):
    kind={}
    for n,k in clothes:
        if k in kind.keys():
            kind[k]+=[n]
        else:
            kind[k]=[n]
    answer=1
    for _, val in kind.items():
        answer*=(len(val)+1)
    return answer-1