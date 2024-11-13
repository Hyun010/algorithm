def solution(s):
    check=["0","1","2","3","4",'5',"6","7","8","9"]
    answer = False
    sc=[]
    for i in range(len(s)):
        if s[i] in check:
            sc.append(s[i])
    if len(s)==4 or len(s)==6:
        if len(sc)!=len(s):
            pass
        else:
            answer=True
    return answer