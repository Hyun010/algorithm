def solution(s):
    answer = True
    p=0
    y=0
    for str in s.lower():
        if str=='p':
            p+=1
            continue
        elif str=='y':
            y+=1
            continue
    print(p,y)
    if p!=y:
        answer=False
    return answer