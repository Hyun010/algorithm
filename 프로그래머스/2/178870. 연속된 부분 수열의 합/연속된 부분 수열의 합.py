def solution(sequence, k):
    answer = []
    start = 0 #시작
    end = 0 #끝
    current_sum = 0 #합 임시저장
    min_length = len(sequence) + 1  # 수열의 최대 길이보다 1 큰 값으로 초기화

    while end < len(sequence):
        current_sum += sequence[end]
        while current_sum > k and start <= end: #k보다 크면 시작을 이동
            current_sum -= sequence[start] #시작이동을 위해 합에서 뺴주기
            start += 1 #이동
        if current_sum == k: #원하는 것
            length = end - start + 1 #길이
            if length < min_length: #길이 비교
                min_length = length #최단 길이
                answer = [start, end]
        end += 1 #끝 이동
    return answer