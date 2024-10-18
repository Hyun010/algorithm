def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        if int(str[s:s+l])>k:
            answer.append(int(str[s:s+l]))
    return answer