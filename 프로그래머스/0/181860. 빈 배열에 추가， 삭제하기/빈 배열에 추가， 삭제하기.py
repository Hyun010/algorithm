def solution(arr, flag):
    answer = []
    for i,boo in enumerate(flag):
        if boo==True:
            for j in range((arr[i]*2)):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer