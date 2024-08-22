def solution(numbers):
    answer = []
    # 주어진 숫자를 이진수 문자열로 변환하는 함수
    def toBinary(number):
        ans = ''
        while number > 0:
            # 나머지를 이용해 이진수 비트를 생성
            ans += str(number % 2)
            number = number // 2  # 정수 나눗셈으로 업데이트

        # 이진수 문자열을 4의 배수 길이로 맞추기 위해 0 추가
        add_zero = 4 - (len(ans) % 4)
        ans += '0' * add_zero  # 부족한 만큼 0을 추가

        return ans[::-1]  # 이진수 문자열을 역순으로 반환

    # 이진수 문자열을 10진수로 변환하는 함수
    def toDecimal(number):
        ans = 0  # 결과를 저장할 변수 초기화
        l = len(number) - 1  # 이진수 문자열의 길이 - 1

        # 이진수 문자열을 순회하며 10진수로 변환
        for n in number:
            ans += (2 ** l) * int(n)  # 2의 거듭제곱과 비트 값을 곱하여 더함
            l -= 1  # 다음 비트로 이동

        return ans  # 최종 10진수 값 반환

    # 주어진 숫자 리스트를 순회
    for num in numbers:
        if num % 2 == 0:
            # 짝수인 경우, 다음 홀수인 num + 1을 추가
            answer.append(num + 1)
        else:
            # 홀수인 경우, 이진수로 변환
            odd_to_binary = toBinary(num)
            # 이진수 문자열의 끝에서부터 0을 찾음
            for i in range(len(odd_to_binary) - 1, -1, -1):
                if odd_to_binary[i] == '0':
                    # 0을 1로 바꾸고 그 다음 비트를 0으로 설정
                    odd_to_binary = odd_to_binary[:i] + '10' + odd_to_binary[i + 2:]
                    # 수정된 이진수를 10진수로 변환하여 결과에 추가
                    answer.append(toDecimal(odd_to_binary))
                    break  # 첫 번째 0만 처리하고 루프 종료

    return answer  # 최종 결과 반환