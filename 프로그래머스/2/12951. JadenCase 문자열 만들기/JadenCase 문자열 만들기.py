def solution(s):
    answer = ''
    check=['0','1','2','3','4','5','6','7','8','9']
    s=s.split(" ")
    temp=[]
    t=''
    for str in s:
        if len(str)>1:
            if str[0] in check:
                t=str.lower()
                temp.append(t)
                t=''
            else:
                t=str[0].upper()+str[1:].lower()
                temp.append(t)
                t=''
        elif len(str) ==1:
            temp.append(str.upper())
        elif str=='':
            temp.append('')
    answer=' '.join(temp)
            
    return answer