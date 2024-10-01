def solution(num, k):
    answer = 0
    for i,n in enumerate(str(num)):
        if int(n)==k:
            answer=i+1
            break
        else:
            answer=-1
    return answer