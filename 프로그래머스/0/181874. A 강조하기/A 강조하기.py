def solution(myString):
    answer = ''
    myString=myString.replace('a','A')
    for i,str in enumerate(myString):
        if str=='A':
            answer+=str
        else:
            answer+=myString[i].lower()
    return answer