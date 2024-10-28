def solution(arr):
    answer = []
    m=min(arr)
    arr.pop(arr.index(m))
    answer=arr
    if answer==[]:
        answer.append(-1)
    return answer