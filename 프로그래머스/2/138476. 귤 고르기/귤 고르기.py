def solution(k, tangerine):
    answer = 0
    total=0
    s={}
    tangerine.sort()
    for i in tangerine:
        if i in s:
            s[i]+=1
        else:
            s[i]=1
    s=sorted(s.values())
    while True:
        total+=s[-1]
        s.pop()
        answer+=1
        if total>=k:
            break
    return answer
#시간초과(길이가 길어질 수록 정렬등이 너무 많다)
# def solution(k, tangerine):
#     answer = 0
#     s=[]
#     total=0
#     tangerine.sort()
#     for i in range(1,max(tangerine)+1):
#         s.append(tangerine.count(i))
#     s.sort()
#     while True:
#         total+=s[-1]
#         s.pop()
#         answer+=1
#         if total>=k:
#             break
#     return answer