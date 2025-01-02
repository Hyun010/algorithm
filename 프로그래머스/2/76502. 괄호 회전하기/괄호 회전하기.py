def isCorrect(s):
    check={'(':')','[':']','{':'}'}
    temp=[]
    for p in s:
        if p in check:
            temp.append(p)
        elif p in check.values():
            if not temp or p !=check[temp.pop()]:
                return False
    return not temp

def leftShift(a,k):
    n=len(a)
    Str=''
    for i in range(n):
        Str+=a[(i+k)%n]
    return Str

def solution(s):
    answer=0
    n=len(s)
    for i in range(n):
        t=leftShift(s,i)
        if isCorrect(t):
            answer+=1
    return answer