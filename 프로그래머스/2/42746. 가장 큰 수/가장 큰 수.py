def solution(numbers):
    numbers_str = list(map(str, numbers)) # 숫자를 문자열로 변환합니다.
    numbers_str.sort(key=lambda x: (x*3)[:4], reverse=True)  # x*3으로 길이를 맞춰 비교
    answer = ''.join(numbers_str)
    # 모든 숫자가 0인 경우 '0'을 반환합니다.
    if answer[0] == '0':
        return '0'
    return answer 