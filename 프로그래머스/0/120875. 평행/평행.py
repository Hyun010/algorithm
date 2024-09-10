def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] =dots #점 초기화
    # 선분 12, 선분 34
    g12 = abs((y2 - y1) / (x2 - x1))
    g34 = abs((y4 - y3) / (x4 - x3))
    # 선분 13, 선분 24
    g13 = abs((y3 - y1) / (x3 - x1))
    g24 = abs((y4 - y2) / (x4 - x2))
    # 선분23, 선분 14
    g14 = abs((y4 - y1) / (x4 - x1))
    g23 = abs((y3 - y2) / (x3 - x2))
    # 셋 중 하나라도 같으면 평행
    if g12 == g34 or g23 == g14 or g13 == g24:
        return 1
    return 0 #아니면 평행 아님