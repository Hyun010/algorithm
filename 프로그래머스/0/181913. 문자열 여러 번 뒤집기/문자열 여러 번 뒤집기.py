def solution(my_string, queries):
    answer = ''
    temp=[]
    my_string=list(my_string)
    for i in range(len(queries)):
        s,e=queries[i][0],queries[i][1]
        for j in range(s,e+1):
            temp.append(my_string[j])
        temp=temp[::-1]
        my_string[:s]=my_string[:s]
        my_string[s:e+1]=temp
        my_string[e+1:]=my_string[e+1:]
        temp=[]
    answer = ''.join(my_string)
    return answer