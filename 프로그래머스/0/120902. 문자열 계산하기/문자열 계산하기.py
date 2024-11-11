def solution(my_string):
    answer = 0
    temp=my_string.split(' ')
    answer+=int(temp[0])
    for i in range(1,len(temp)+1):
        if i!=len(temp):
            if temp[i]=='+':
                answer+=int(temp[i+1])
            elif temp[i]=='-':
                answer-=int(temp[i+1])
    return answer