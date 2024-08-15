def solution(order):
    answer = 0  #들어가는 상자 개수
    t=[] #보조 컨테이너 벨트
    for n in range(1,len(order)+1): #숫자만큼 돌린다
        t.append(n) #보조에 넣는다
        while t and t[-1]==order[answer]: #보조에 존재하며, 마지막이 순서와 맞다면 트럭에 실어 넣는다
            t.pop() #보조에서 뺀다
            answer+=1 #다음 순서로 넘어간다
    
    return answer  
