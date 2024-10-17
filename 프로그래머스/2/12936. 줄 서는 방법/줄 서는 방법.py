#팩토리얼 계산
def factorial(x): 
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def solution(n, k):
    answer = []
    nums = list(range(1, n + 1)) #줄 세우기
    k -= 1 #k는 1부터 시작->0으로 초기화
    while n > 0:
        fact = factorial(n - 1) #n 팩토리얼 계산(각 자리의 경우의 수)
        index = k // fact #현재 자리 인덱스
        answer.append(nums[index]) #현재 자리 맞는 숫자 가져와서 추가
        nums.pop(index) #선택된 숫자 제거
        k %= fact #k업데이트
        n -= 1 #n업데이트
    return answer