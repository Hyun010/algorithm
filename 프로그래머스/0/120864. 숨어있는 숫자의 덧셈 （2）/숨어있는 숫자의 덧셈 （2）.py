def solution(my_string):
    answer = []
    d=['0','1','2','3','4','5','6','7','8','9']
    temp=[]
    temp_s=[]
    tmp=''
    s=0
    for str in my_string:
        if str in d:
            temp.append(str)
        else:
            temp.append(',')
    for str in temp:
        if str in d:
            temp_s.append(str)
        elif str==',':
            while temp_s!=[]:
                tmp+=temp_s.pop()
            tmp=tmp[::-1]
            print(tmp)
            answer.append(tmp)
            tmp=''
    while temp_s!=[]:
        tmp+=temp_s.pop()
    tmp=tmp[::-1]
    print(tmp)
    answer.append(tmp)
    tmp=''
    
    answer=list(filter(None,answer))
    if answer==[]:
        s=0
    else:
        for i in answer:
            s+=int(i)
    return s