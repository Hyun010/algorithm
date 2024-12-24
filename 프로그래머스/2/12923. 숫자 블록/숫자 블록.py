def solution(begin, end):
    answer = []
    for position in range(begin, end + 1):
        if position == 1: #1번 항상 0
            answer.append(0)
            continue
        block = 1 #초기값 1
        limit = int(position**0.5) #효율성->제곱근까지만 탐색
        for divisor in range(2, limit + 1):
            if position % divisor == 0: #약수를 찾으면
                paired_divisor = position // divisor
                if paired_divisor <= 10000000: #블록 제한 조건 확인
                    block = max(block, paired_divisor)
                    break
                block = max(block, divisor)
        answer.append(block)
    return answer