def solution(arr):
    answer = []
    idx_f=0
    idx_e=0
    for i,num in enumerate(arr):
        if num==2:
            idx_f=i
            break
    for i,num in enumerate(arr[::-1]):
        if num==2:
            idx_e=len(arr)-(i+1)
            break
    if idx_f==0 and idx_e==0:
        answer.append(-1)
    else:
        for i in range(idx_f,idx_e+1):
            answer.append(arr[i])
    return answer