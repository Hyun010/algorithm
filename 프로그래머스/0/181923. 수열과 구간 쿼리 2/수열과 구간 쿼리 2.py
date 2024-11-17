def solution(arr, queries):
    answer = []
    t=[]
    for i in range(len(queries)):
        s,e,k=queries[i][0],queries[i][1],queries[i][2]
        for j in range(s,e+1):
            if arr[j]>k:
                t.append(arr[j])
        if t==[]:
            answer.append(-1)
        else:
            answer.append(min(t))
        t=[]
    return answer