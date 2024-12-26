def solution(name):
    n = len(name)
    #알파벳 조작횟수
    def up_down_cost(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
    #알파벳 조작횟수 합
    move_count = sum(up_down_cost(char) for char in name)
    min_horizontal_moves = n - 1 #최대로 오른쪽으로만 이동했을 때
    for i in range(n):
        #다음으로 연속된 'A'의 끝 부분 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        #i: 현재 위치까지 이동
        #n - next_idx: 남은 부분까지 이동 후 돌아가기
        distance = 2 * i + n - next_idx #왼쪽 -> 오른쪽
        min_horizontal_moves = min(min_horizontal_moves, distance)
        #반대 방향(오른쪽 -> 왼쪽)
        distance = i + 2 * (n - next_idx)
        min_horizontal_moves = min(min_horizontal_moves, distance)
    return move_count + min_horizontal_moves