def solution(n, stations, w):
    answer = 0
    current = 1  # 현재 커버되지 않는 아파트의 시작 위치
    # 기존 기지국이 설치된 아파트를 순회
    for station in stations:
        # 기지국이 커버할 수 있는 범위의 끝 위치
        coverage_start = station - w
        coverage_end = station + w
        
        # 현재 커버되지 않는 아파트가 기지국의 커버 범위에 포함되지 않는 경우
        while current < coverage_start:
            # 새로운 기지국을 설치해야 하는 아파트의 위치
            answer += 1
            # 새 기지국의 커버 범위 업데이트
            current += (2 * w + 1)  # 새 기지국이 커버하는 범위
            
        # 현재 아파트의 다음 위치로 이동
        current = coverage_end + 1  # 다음 커버되지 않는 아파트로 이동
        print(current)
    
    # 마지막 기지국 커버 범위 이후의 아파트 처리
    if current <= n:
        # 현재 아파트가 n 이하라면 추가 기지국 설치
        answer += (n - current + 1 + (2 * w)) // (2 * w + 1)
    
    return answer