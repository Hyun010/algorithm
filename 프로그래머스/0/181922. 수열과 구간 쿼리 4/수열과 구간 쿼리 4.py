def solution(arr, queries):
    for q in queries:
        s,e,k=q[0],q[1],q[2]
        for j in range(s,e+1):
            if j%k==0:
                arr[j]+=1
    return arr