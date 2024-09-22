def solution(my_string):
    answer = []
    for str in my_string:
        if ord(str)<=57:
            answer.append(int(str))
    answer.sort()
    return answer