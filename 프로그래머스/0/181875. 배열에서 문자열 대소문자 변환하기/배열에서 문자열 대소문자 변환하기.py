def solution(strArr):
    answer = []
    for i,str in enumerate(strArr):
        if i%2==0:
            answer.append(str.lower())
        else:
            answer.append(str.upper())
    return answer