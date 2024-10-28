def solution(arr):
    answer = []
    idx=0
    for i in range(11):
        if len(arr)<=2**i:
            idx=i
            break
    if len(arr)!=2**idx:
        for i in range((2**idx)-len(arr)):
            arr.append(0)
        answer=arr
    else:
        answer=arr
    return answer