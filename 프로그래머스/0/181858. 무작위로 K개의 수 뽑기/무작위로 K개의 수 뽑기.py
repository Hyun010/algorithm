def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
        if len(answer)==k:
            break

    if len(answer)!=k:
        while len(answer)!=k:
            answer.append(-1)
    return answer