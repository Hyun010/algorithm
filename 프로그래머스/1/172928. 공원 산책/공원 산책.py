def solution(park, routes):
    height = len(park) #세로
    width = len(park[0]) #가로
    position = None #위치
    #시작 위치 찾기
    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                position = (i, j)
                break
        if position:
            break
    #명령어
    for route in routes:
        direction, distance = route.split() #파싱
        distance = int(distance) #정수변환
        #방향에 따른 위치 이동 정의
        if direction == 'N':
            new_position = (position[0] - distance, position[1])
        elif direction == 'S':
            new_position = (position[0] + distance, position[1])
        elif direction == 'W':
            new_position = (position[0], position[1] - distance)
        elif direction == 'E':
            new_position = (position[0], position[1] + distance)
        #새 위치 공원내 존재하는지 확인
        if 0 <= new_position[0] < height and 0 <= new_position[1] < width:
            obstacle = False #장애물 확인 변수
            #방향별 처리
            if direction == 'N':
                for k in range(1, distance + 1):
                    if park[position[0] - k][position[1]] == 'X': #장애물
                        obstacle = True #표시
                        break
            elif direction == 'S':
                for k in range(1, distance + 1):
                    if park[position[0] + k][position[1]] == 'X':
                        obstacle = True
                        break
            elif direction == 'W':
                for k in range(1, distance + 1):
                    if park[position[0]][position[1] - k] == 'X':
                        obstacle = True
                        break
            elif direction == 'E':
                for k in range(1, distance + 1):
                    if park[position[0]][position[1] + k] == 'X':
                        obstacle = True
                        break
            if not obstacle: #장애물 없으면 위치 업데이트
                position = new_position
    return [position[0], position[1]]