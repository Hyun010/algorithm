def solution(strArr):
    answer = 0
    s=[0]*len(strArr)
    for str in strArr:
        s[len(str)]+=1
    answer=max(s)
    return answer