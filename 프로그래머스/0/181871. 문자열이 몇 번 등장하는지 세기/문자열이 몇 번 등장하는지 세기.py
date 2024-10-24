def solution(myString, pat):
    answer =0
    temp=''
    for i in range(len(myString)):
        temp=myString[i:i+len(pat)]
        if temp==pat:
            answer+=1
    return answer