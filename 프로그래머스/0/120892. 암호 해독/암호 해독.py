def solution(cipher, code):
    answer = ''
    for i,str in enumerate(cipher):
        if (i+1)%code==0:
            answer+=str
    return answer