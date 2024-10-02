def solution(number):
    answer = 0
    for num in number:
        answer+=int(num)
    answer%=9
    return answer