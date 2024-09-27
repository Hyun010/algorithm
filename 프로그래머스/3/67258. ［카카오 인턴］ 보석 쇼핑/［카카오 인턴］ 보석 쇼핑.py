def solution(gems):
    unique_gems = set(gems) #종류
    total_types = len(unique_gems) #종류 수
    left = 0 #시작
    right = 0 #끝
    gem_count = {} #종류,수 담을 딕셔너리
    min_length = float('inf') #최소 길이를 무한대로 초기화(최대)
    answer = [0, 0] #초기화
    while right < len(gems): #끝 포인터가 보석수 아래일때까지 확인
        gem_count[gems[right]] = gem_count.get(gems[right], 0) + 1 #끝에 종류와 수 증가
        right += 1 #끝 증가
        while len(gem_count) == total_types: #키 수가 전체 종류와 동일하면 
            current_length = right - left #현재 길이
            if current_length < min_length: #현재 길이와 최소길이 확인
                min_length = current_length #교체
                answer = [left + 1, right] #순서는 1부터 시작
            gem_count[gems[left]] -= 1 #새로운 구간을 확인을 위해 시작 조정
            if gem_count[gems[left]] == 0: #시작이 0면 종류와 수를 제거
                del gem_count[gems[left]]
            left += 1 #시작 증가
    return answer #모든 구간 확인후 가장 짧은 구간 리턴