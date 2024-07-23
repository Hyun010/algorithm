def solution(prices):
    l=len(prices) #길이
    answer = [i for i in range(l-1,-1,-1)] #최댓값으로 초기화, -1은 0까지 하기 위함, -1 전체에서 자기자신 뺴고 앞선 수 뺴기
    s=[0] #스택 초기화
    for i in range(1,l): #시간경과
        while s and prices[s[-1]]>prices[i]: #스택이 존재하며 현재값과 미래값 비교해서 크면
            j=s.pop() #떨어진 시간
            answer[j]=i-j #현재시간에 시간-떨어진시간->유지시간
        s.append(i)#다음시간 추가
    return answer