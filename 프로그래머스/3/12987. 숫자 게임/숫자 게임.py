def solution(a, b):
    # A팀과 B팀의 숫자를 정렬
    a.sort()
    b.sort()
    answer = 0
    j = 0  # B팀의 인덱스
    # A팀의 각 숫자에 대해 B팀의 숫자를 비교
    for am in a:
        # B팀의 숫자가 남아있고, 현재 B팀의 숫자가 A팀의 숫자보다 클 경우
        while j < len(b) and b[j] <= am:
            j += 1  # 다음 숫자  
        # B팀의 인덱스가 범위를 초과하지 않고, 현재 B팀의 숫자가 A팀의 숫자보다 큰 경우
        if j < len(b):
            answer += 1  # 승점 추가
            j += 1  #다음 숫자
    return answer