def solution(s):
    answer = ''
    al=[]
    for str in s:
        if s.count(str)==1:
            al.append(str)
    al.sort()
    answer=''.join(al)
    return answer