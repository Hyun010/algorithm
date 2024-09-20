def solution(n):
    answer = ''
    numbers = ['4', '1', '2'] #숫자 나머지 순 0:4, 1:1, 2:2로 저장
    while n > 0:
        answer = numbers[n % 3] + answer #나머지의 위치로 숫자 저장
        n = (n - 1) // 3 #몪으로 자리수 늘여주기, n-1은 0위치 맞추기
    return answer
