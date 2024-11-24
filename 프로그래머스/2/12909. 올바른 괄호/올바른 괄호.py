def solution(s):
    t=[]
    for i in range(len(s)):
        if t==[]:
            if s[i]=='(':
                t.append(s[i])
            else:
                return False
        else:
            if s[i]=='(':
                t.append(s[i])
            else:
                t.pop()
        
    if t !=[]:
        return False
    return True