def solution(s):
    answer = ''
    temp=sorted(s,reverse=True)
    for t in temp:
        answer+=t
    return answer