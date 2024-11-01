def hanoi(n, start, target, mid, moves):
    if n == 1: #원판 1개(탈출)
        moves.append([start, target]) #마지막 이동
        return
    hanoi(n - 1, start, mid, target, moves) #n-1개 원판 시작->보조
    moves.append([start, target]) #가장 큰 원판 목표로 이동
    hanoi(n - 1, mid, target, start, moves) #n-1개 원판 보조->목표

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer) #시작 n개 1->3, 보조 2, 이동경로 저장 배열
    return answer