def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)} #현재 순위
    for call in callings:
        current_rank = rank[call] #호출된 현재 순위
        #1등 아닌 경우
        if current_rank > 0:
            overtaken_player = players[current_rank - 1] #추월당한 사람
            players[current_rank], players[current_rank - 1] = players[current_rank - 1], players[current_rank] #순위 업데이트
            rank[call] -= 1 #호출된 선수 감소
            rank[overtaken_player] += 1 #추월당한 선수 증가
    return players #순서대로 배열 리턴