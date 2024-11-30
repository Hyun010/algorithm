def solution(s):
    answer = []
    s=s.split(' ')
    for t in s:
        temp=''
        for i in range(len(t)):
            if i%2==0:
                temp+=t[i].upper()
            else:
                temp+=t[i].lower()
        answer.append(temp)
    answer=' '.join(answer)
    return answer


#공백이 제거되면 안된다 끝에도 공백이 살아 있어야한다
# def solution(s):
#     answer = ''
#     s=s.split(' ')
#     for t in s:
#         for i in range(len(t)):
#             if i%2==0:
#                 answer+=t[i].upper()
#             else:
#                 answer+=t[i].lower()
#         answer+=' '
#     answer=answer.rstrip()
#     return answer