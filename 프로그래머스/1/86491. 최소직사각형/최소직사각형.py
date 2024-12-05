def solution(sizes):
    answer = 0
    w,h=0,0
    for x,y in sizes:
        if x>y:
            x,y=y,x
        if w<x:
            w=x
        if h<y:
            h=y
    answer=w*h
    return answer