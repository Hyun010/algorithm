def solution(A, B):
    answer = 0
    temp=''
    for i in range(len(A)):
        temp+=A[i]
    while True:
        if temp==B:
            break
        temp=temp[-1]+temp[0:len(temp)-1]
        answer+=1
        if temp==A:
            answer=-1
            break
        
    return answer