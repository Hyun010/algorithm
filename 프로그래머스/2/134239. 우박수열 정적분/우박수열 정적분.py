#우박수열 생성
def generate_collatz_sequence(k):
    sequence = [k]
    while k != 1:
        if k % 2 == 0: #짝수
            k //= 2
        else: #홀수
            k = k * 3 + 1
        sequence.append(k)
    return sequence

#넓이 계산
def calculate_area(points):
    areas = []
    for i in range(len(points) - 1):
        #두 점 사이의 사다리꼴 넓이
        h = 1 #x간격은 항상 1
        area = (points[i] + points[i + 1]) / 2 * h
        areas.append(area)
    return areas

def solution(k, ranges):
    answer = []
    #우박수열 생성
    collatz_sequence = generate_collatz_sequence(k)
    #사다리꼴 넓이 계산
    areas = calculate_area(collatz_sequence)
    total_steps = len(areas) #전체 길이
    for start, end in ranges:
        #끝점은 음tn->total_steps 더하기
        actual_end = total_steps + end
        if start > actual_end: #유효하지 않은 구간
            answer.append(-1.0)
        else:
            #지정된 구간의 넓이 합산
            result = sum(areas[start:actual_end])
            answer.append(float(result))
    return answer