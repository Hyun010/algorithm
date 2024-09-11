def solution(myString):
    answer = []
    new=myString.split('x')
    for i in new:
        answer.append(len(i))
    return answer