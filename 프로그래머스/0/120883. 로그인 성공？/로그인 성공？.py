def solution(id_pw, db):
    answer = ''
    s=[]
    if id_pw in db:
        answer='login'
    else:
        for i in range(len(db)):
            if id_pw[0]==db[i][0]:
                s.append(i)
        if s==[]:
            answer='fail'
        else:
            for i in s:
                if db[i][1] != id_pw[1]:
                    answer='wrong pw'
    return answer





#1번 실패, 우선순위 실패인듯하다
# def solution(id_pw, db):
#     answer = ''
#     for i in range(len(db)):
#         if id_pw in db:
#             answer='login'
#         else:
#             if id_pw[0]==db[i][0]:
#                 if id_pw[1] != db[i][1]:
#                     answer='wrong pw'
#             else:
#                 answer='fail'
#     return answer