def solution(my_string, num1, num2):
    answer = ''
    str1=''
    str2=''
    for i,str in enumerate(my_string):
        if i==num1:
            str1+=str
        if i==num2:
            str2+=str
    for i,str in enumerate(my_string):
        if i==num1:
            answer+=str2
        elif i==num2:
            answer+=str1
        else:
            answer+=str
    return answer