def solution(n, build_frame):
    answer = []
    #설치 가능 확인 함수
    def can_place(x, y, a):
        if a == 0: #기둥
            #바닥 위에 있거나, 다른 기둥 위에 있거나, 보의 한쪽 끝 위에 있어야 함
            return y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer
        else: #보
            #기둥 위에 있거나, 양쪽 끝이 다른 보와 연결되어 있어야 함
            return ([x, y - 1, 0] in answer or
                    [x + 1, y - 1, 0] in answer or
                    ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer))
    #구조물이 유효한지 확인하는 함수
    def is_valid():
        for x, y, a in answer:
            if not can_place(x, y, a):
                return False
        return True
    for x, y, a, b in build_frame:
        if b == 1: #설치
            answer.append([x, y, a])
            if not is_valid(): #유효하지 않으면 제거
                answer.remove([x, y, a])
        else: #삭제
            answer.remove([x, y, a])
            if not is_valid(): #유효하지 않으면 다시 추가
                answer.append([x, y, a])
    return sorted(answer)