def solution(emergency):
    answer = [0]*len(emergency)
    el=sorted(emergency,reverse=True)
    for i in range(len(el)):
        answer[emergency.index(el[i])]=i+1
    return answer