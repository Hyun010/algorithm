def solution(s):
    answer = 0
    t=[]
    s=s.split(' ')
    for str in s:
        if str=='Z':
            t.pop()
        else:
            t.append(str)
    for num in t:
        answer+=int(num)
    return answer