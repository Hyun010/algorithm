def solution(numbers, hand):
    answer = ""
    left='*' #왼손 초기화
    right='#' #오른손 초기화
    # 키패드에서 각 숫자의 위치를 정의
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    #거리 계산
    def calculate_distance(position1, position2):
        x1, y1 = position1
        x2, y2 = position2
        return abs(x1 - x2) + abs(y1 - y2)
    
    for number in numbers:
        if number in [1, 4, 7]: #왼손 사용
            answer += "L"
            left = number
        elif number in [3, 6, 9]: #오른손 사용
            answer += "R"
            right = number
        else: #가운데 거리확인, 손잡이따라 처리
            left_distance = calculate_distance(keypad[left], keypad[number]) #왼쪽 거리
            right_distance = calculate_distance(keypad[right], keypad[number]) #오른쪽 거리
            if left_distance < right_distance: #왼쪽 가까운 경우
                answer += "L"
                left = number
            elif right_distance < left_distance: #오른쪽이 가까운 경우
                answer += "R"
                right = number
            else: #거리가 동일할 경우
                if hand == "right": #오르손 주
                    answer += "R"
                    right = number
                else: #왼손 주
                    answer += "L"
                    left = number
    return answer