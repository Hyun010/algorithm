def solution(arr1, arr2):
    n=len(arr1)
    m=len(arr2[0])
    cnt=len(arr1[0])
    answer = [[0]*m for _ in range(n)]
    s1=[]
    s2=[]
    for i in range(n):
        temp=[]
        for j in range(cnt):
            temp.append(arr1[i][j])
        s1.append(temp)
        
    for j in range(m):
        temp=[]
        for i in range(len(arr2)):
            temp.append(arr2[i][j])
        s2.append(temp)
    
    for i in range(n):
        for j in range(m):
            v1=s1[i]
            v2=s2[j]
            sum=0
            for idx in range(cnt):
                sum+=v1[idx]*v2[idx]
                
            answer[i][j]=sum
    return answer