from collections import deque
def solution(cacheSize, cities):
    answer=0
    s=deque([])
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
    if cacheSize==0:
        answer=len(cities)*5
    else:
        for i in cities:
            if i not in s:
                s.append(i)
                answer+=5
                if len(s)>cacheSize:
                    s.popleft()
                
            else:
                s.remove(i)
                s.append(i)
                answer+=1
                if len(s)>cacheSize:
                    s.popleft()
    return answer