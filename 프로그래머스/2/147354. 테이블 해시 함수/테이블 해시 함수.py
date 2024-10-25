def solution(data, col, row_begin, row_end):
    answer = 0
    #col값 기준 오름, 기본키 기준 내림으로 정렬한 데이터
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0])) #col 인덱스 0
    for i in range(row_begin, row_end + 1):
        current_row = sorted_data[i - 1] #i행 인덱스 0로 맞추기
        S_i = sum(value % i for value in current_row) #S_i 계산(나머지 합)
        answer ^= S_i #XOR 연산으로 업데이트
    return answer