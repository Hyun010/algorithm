#거리두기 확인
def check_distancing(place):
    #상하좌우 검사(맨해튼 거리1)
    directions_1 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #직선, 대각선 검사(맨해튼 거리2)
    directions_2_straight = [(-2, 0), (2, 0), (0, -2), (0, 2)] #직선
    directions_2_diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)] #대각선
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P': #사람
                #거리 1 탐색
                for dx, dy in directions_1:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        return 0 #거리 1이면 실패
                #거리 2 탐색 (직선)
                for dx, dy in directions_2_straight:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        #중간 파티션X면 실패
                        if place[(i + ni) // 2][(j + nj) // 2] != 'X':
                            return 0
                #거리 2 탐색 (대각선)
                for dx, dy in directions_2_diagonal:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and place[ni][nj] == 'P':
                        #대각선은 두 곳 존재해야 안전
                        if place[i][nj] != 'X' or place[ni][j] != 'X':
                            return 0
    return 1 #모든 케이스 통과면 거리두기O

def solution(places):
    answer = []
    for place in places:
        answer.append(check_distancing(place))
    return answer