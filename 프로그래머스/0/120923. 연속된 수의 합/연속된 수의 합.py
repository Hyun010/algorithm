def solution(num, total):
    answer = []
    cnt=0
    for i in range(1,num):
        cnt+=i
    first=int((total-cnt)/num)
    for i in range(0,num):
        answer.append(first+i)
    return answer