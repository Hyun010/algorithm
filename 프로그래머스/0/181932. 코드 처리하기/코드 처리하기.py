def solution(code):
    answer = ''
    mode=0
    code=list(code)
    for idx,str in enumerate(code):
        if mode==0:
            if str=='1':
                mode=1
            else:
                if idx%2==0:
                    answer+=str
        else:
            if str=='1':
                mode=0
            else:
                if idx%2==1:
                    answer+=str
    if answer=='':
        answer='EMPTY'
    return answer