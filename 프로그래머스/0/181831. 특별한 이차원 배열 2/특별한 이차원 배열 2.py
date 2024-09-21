def solution(arr):
    answer = 0
    p=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                if arr[i][j]==arr[j][i]:
                    p.append(1)
                else:
                    p.append(0)
    if all(p):
        answer=1
    return answer