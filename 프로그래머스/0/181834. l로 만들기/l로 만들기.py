def solution(myString):
    answer = ''
    for i,str in enumerate(myString):
        if str<'l':
            answer+='l'
        else:
            answer+=str
    return answer