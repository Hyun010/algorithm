def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        s,e=map(int,parts[i])
        answer+=my_strings[i][s:e+1]
    return answer