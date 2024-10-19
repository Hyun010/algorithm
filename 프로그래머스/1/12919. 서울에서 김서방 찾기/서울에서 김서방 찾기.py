def solution(seoul):
    answer = ''
    f=0
    for i,str in enumerate(seoul):
        if str=='Kim':
            f=i
            break
    answer=f'김서방은 {f}에 있다'
    return answer