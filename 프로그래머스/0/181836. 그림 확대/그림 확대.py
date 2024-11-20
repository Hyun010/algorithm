def solution(picture, k):
    answer = []
    temp=''
    for str in picture:
        for s in str:
            temp+=(s*k)
        for i in range(k):
            answer.append(temp)
        temp=''
    return answer