def solution(my_string):
    answer = ''
    temp=sorted(my_string.lower())
    for t in temp:
        answer+=t
    return answer