from heapq import heappush, heappop

def solution(operations):
    answer = []
    heap=[]
    for i in operations:
        a,n=i.split()
        n=int(n)
        if a=='I':
            heappush(heap,n)
        else:
            if heap:
                if n==-1:
                    heappop(heap)
                else:
                    heap.pop()
    heap.sort()
    if heap:
        answer=[heap[-1],heap[0]]
    else:
        answer=[0,0]
    return answer