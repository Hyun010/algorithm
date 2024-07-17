import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) #스코빌 지수를 히입 자료형으로 변경(우선순위 큐), 최소히입
    while scoville[0]<K: #최소 스코빌이 K를 넘지 않을 때
        answer+=1 #섞기
        m1=heapq.heappop(scoville) #제일 작은 스코빌, 제거
        m2=heapq.heappop(scoville) #그 다음 작은 스코빌, 제거
        heapq.heappush(scoville,m1+(m2*2)) #새로운 음식 추가
        if (len(scoville)==2) and ((scoville[0]+scoville[1]*2)<K): #모든 음식의 스코빌 지수를 K이상 만들 수 없는 경우)
            return -1
    return answer