def solution(X, Y):
    count_X = [0] * 10 #0~9 개수 리스트 초기화
    count_Y = [0] * 10 #0~9 개수 리스트 초기화
    common_digits = [] #공통 수 리스트 초기화
    for digit in X: 
        count_X[int(digit)] += 1 #각 0~9 수 카운트
    for digit in Y:
        count_Y[int(digit)] += 1 #각 0~9 수 카운트
    for i in range(10):
        common_count = min(count_X[i], count_Y[i]) #각 수의 최솟값이 공통 조건
        common_digits.extend([str(i)] * common_count) #각 수 개수만큼 리스트에 추가
    if not common_digits: #공통 수가 없으면 -1 리턴
        return "-1"
    common_digits.sort(reverse=True) #큰수를 위한 내림차순 정렬
    if common_digits.count('0') == len(common_digits): #0은 한개로만 출력
        return "0"
    return ''.join(common_digits) #하나의 숫자 문자열로 출력