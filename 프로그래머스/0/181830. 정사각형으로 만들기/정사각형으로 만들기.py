def solution(arr):
    answer = [[]]
    n=len(arr)#행의 수
    m=len(arr[0]) #열의 수
    if n>m:
        answer = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                try:
                    if arr[i][j]!=0:
                        answer[i][j]=arr[i][j]
                except IndexError:
                    pass

    elif n<m:
        answer = [[0]*m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                try:
                    if arr[i][j]!=0:
                        answer[i][j]=arr[i][j]
                except IndexError:
                    pass
    else:
        answer=arr
    return answer