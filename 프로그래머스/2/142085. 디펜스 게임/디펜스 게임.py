import heapq

def solution(n, k, enemy):
    answer = 0
    max_heap = []
    for e in enemy:
        n -= e #병사 소모
        heapq.heappush(max_heap, -e) #최적화 사용
        answer += 1
        if n < 0: #병사 부족시
            if k > 0: #무적권
                n += -heapq.heappop(max_heap)
                k -= 1
            else: #무적권X, 병사X 종료
                answer -= 1
                break
    return answer