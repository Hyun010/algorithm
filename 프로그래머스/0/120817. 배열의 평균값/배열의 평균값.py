def solution(numbers):
    answer = 0
    for number in numbers:
        answer+=number
        
    answer=round(answer/len(numbers),1)
    return answer