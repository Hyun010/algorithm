def solution(numbers, num1, num2):
    answer = []
    s=slice(num1,num2+1)
    answer=numbers[s]
    return answer