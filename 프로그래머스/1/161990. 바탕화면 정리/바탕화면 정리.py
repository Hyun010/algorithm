def solution(wallpaper):
    position = [] #파일 위치
    rows = len(wallpaper) #열 길이
    cols = len(wallpaper[0]) #행 길이
    for r in range(rows):
        for c in range(cols):
            if wallpaper[r][c] == '#': #파일 위치
                position.append((r, c))
    lux = min(pos[0] for pos in position) #최상단
    luy = min(pos[1] for pos in position) #최좌측
    rdx = max(pos[0] for pos in position) #최하단
    rdy = max(pos[1] for pos in position) #최우측
    return [lux, luy, rdx + 1, rdy + 1]