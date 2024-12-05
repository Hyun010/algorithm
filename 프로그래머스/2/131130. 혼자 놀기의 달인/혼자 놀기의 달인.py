def solution(cards):
    n = len(cards)
    visited = [False] * n #방문기록
    group_sizes = [] #박스그룹 크기
    for i in range(n):
        if not visited[i]: #방문X
            size = 0
            current = i
            while not visited[current]:
                visited[current] = True #방문 처리
                current = cards[current] - 1 #카드번호를 다음 이동 설정
                size += 1 #그룹 크기 증가
            group_sizes.append(size)
    if len(group_sizes) < 2: #2개이상 곱셈가능, 아니면 0리턴
        return 0
    group_sizes.sort(reverse=True) #최고 큰값을 위한 내림차순정렬
    return group_sizes[0] * group_sizes[1]