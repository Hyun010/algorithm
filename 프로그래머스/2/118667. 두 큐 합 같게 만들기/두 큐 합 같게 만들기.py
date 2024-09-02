from collections import deque

def solution(queue1, queue2):
    # 두 큐를 deque로 변환
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    # 두 큐의 합 계산
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 전체 합 계산
    total_sum = sum1 + sum2

    # 두 큐의 합이 홀수일 경우, 절대 같게 만들 수 없음
    if total_sum % 2 != 0:
        return -1

    # 목표는 각 큐의 합을 전체 합의 절반으로 만드는 것
    target = total_sum // 2

    # 작업 횟수 초기화
    answer = 0
    max_operations = len(queue1)*3 # 최악의 경우 작업 횟수

    while answer < max_operations:
        if sum1 == target: #목표면 탈출 조건
            return answer
        
        # 현재 합이 목표보다 작으면 queue2
        if sum1 < target:
            element = queue2.popleft()
            queue1.append(element)
            sum1 += element
            sum2 -= element
        else:  # 현재 합이 목표보다 크면 queue1
            element = queue1.popleft()
            queue2.append(element)
            sum1 -= element
            sum2 += element
        
        # 작업 횟수 증가
        answer += 1

    # 목표를 달성할 수 없다면 -1 반환
    return -1