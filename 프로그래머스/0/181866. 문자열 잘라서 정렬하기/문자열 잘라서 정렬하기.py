def solution(myString):
    answer = []
    temp=myString.split('x')
    for i,t in enumerate(temp):
        if t!='':
            answer.append(t)
    answer.sort()
    return answer