def solution(strings, n):
    strings.sort(key=lambda x:(x[n],x))
    return strings

#인덱스 같은 문자 여럿일 경우 사전 순이라는 것을->두번째 인덱스로 처리한 것
# def solution(strings, n):
#     answer = []
#     temp=[]
#     t=[]
#     for str in strings:
#         temp.append(str[n])
#     for str in temp:
#         t.append(str)
#     temp.sort()
#     for i in range(len(temp)):
#         answer.append(strings[t.index(temp[i])])
#     return answer