#소수확인 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#소수 찾는 함수
def find_numbers(numbers, current, visited, answer):
    if current:  
        num = int(current)
        if is_prime(num):
            answer.add(num)  # 소수일 경우 집합에 추가

    for i in range(len(numbers)):
        if not visited[i]:  # 방문하지 않은 숫자만 사용
            visited[i] = True  # 방문 표시
            find_numbers(numbers, current + numbers[i], visited, answer)  # 재귀 호출
            visited[i] = False  # 방문 해제

def solution(numbers):
    answer = set()  # 소수를 저장할 집합
    visited = [False] * len(numbers)  # 숫자 방문 여부

    find_numbers(numbers, "", visited, answer)  # 숫자 찾기 시작

    return len(answer)  # 소수의 개수 반환