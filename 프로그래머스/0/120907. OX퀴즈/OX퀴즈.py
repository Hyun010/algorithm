def solution(quiz):
    answer = []
    for s in quiz:
        x,op,y,eq,z=s.split(' ')
        if op=='+':
            t=int(x)+int(y)
            if t==int(z):
                answer.append("O")
            else:
                answer.append("X")
            t=0
        else:
            t=int(x)-int(y)
            if t==int(z):
                answer.append("O")
            else:
                answer.append("X")
            t=0
    return answer