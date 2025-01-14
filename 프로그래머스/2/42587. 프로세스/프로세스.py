from collections import deque

def solution(priorities, location):
    answer = 0
    que=deque(enumerate(priorities))
    while que:
        i,p=que.popleft()
        if any(p<pp for _,pp in que):
            que.append((i,p))
        else:
            answer+=1
            if i==location:
                break
    return answer