from collections import deque #큐사용

def solution(x, y, n):
    answer = 0 
    # 큐 초기화
    queue = deque([(x, 0)])  # (현재 값, 연산 횟수)
    visited = set()  # 방문한 숫자를 저장할 집합
    visited.add(x)  # 시작 숫자 추가

    while queue:
        current, steps = queue.popleft()

        # 현재 값이 목표 값 y와 같다면 최소 연산 횟수 반환
        if current == y:
            return steps
        
        # 다음 연산: x에 n 더하기
        next_add = current + n
        if next_add <= y and next_add not in visited:
            visited.add(next_add)
            queue.append((next_add, steps + 1))

        # 다음 연산: x에 2 곱하기
        next_mul2 = current * 2
        if next_mul2 <= y and next_mul2 not in visited:
            visited.add(next_mul2)
            queue.append((next_mul2, steps + 1))

        # 다음 연산: x에 3 곱하기
        next_mul3 = current * 3
        if next_mul3 <= y and next_mul3 not in visited:
            visited.add(next_mul3)
            queue.append((next_mul3, steps + 1))

    # 모든 경우를 시도했지만 y에 도달하지 못한 경우 -1 반환
    return -1
