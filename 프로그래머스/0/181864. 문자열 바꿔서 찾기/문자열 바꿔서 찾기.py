def solution(myString, pat):
    answer = 0
    temp=str.maketrans('AB','BA')
    new=myString.translate(temp)
    if pat in new:
        answer=1
    else:
        answer=0
    return answer