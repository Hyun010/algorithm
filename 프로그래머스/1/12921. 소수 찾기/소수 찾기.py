def solution(n):
    answer = 0
    all_list=[True]*(n+1) #전체 초기화 True
    for i in range(2,int(n**0.5)+1): #루트n보다 작은 모든 소수로 나누어 떨어지지 않으면 n은 소수
        if all_list[i]==True:
            for j in range(i*i,n+1,i):
                all_list[j]=False
    answer=len([i for i in range(2,n+1) if all_list[i]==True])
    return answer