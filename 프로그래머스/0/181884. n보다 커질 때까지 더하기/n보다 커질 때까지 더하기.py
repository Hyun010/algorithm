def solution(numbers, n):
    answer = 0
    sum_num=0
    for num in numbers:
        sum_num+=num
        if sum_num>n:
            answer=sum_num
            break
    return answer