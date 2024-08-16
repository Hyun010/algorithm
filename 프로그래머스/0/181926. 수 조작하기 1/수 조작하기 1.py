def solution(n, control):
    answer = 0
    for str in control:
        if str=='w':
            n+=1
        elif str=='s':
            n-=1
        elif str=='d':
            n+=10
        elif str=='a':
            n-=10
    answer=n
    return answer