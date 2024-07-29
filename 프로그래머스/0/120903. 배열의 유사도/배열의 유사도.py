def solution(s1, s2):
    answer = 0
    cnt=0
    for s_2 in s2:
        for s_1 in s1:
            if s_1 == s_2:
                cnt+=1          
    answer=cnt
    return answer