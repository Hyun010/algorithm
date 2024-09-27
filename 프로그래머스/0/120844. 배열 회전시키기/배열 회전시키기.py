from collections import deque

def solution(numbers, direction):
    answer = []
    q = deque(numbers)
    if direction=='right':
        q.rotate(1)
    else:
        q.rotate(-1)
    for num in q:
        answer.append(num)
    return answer