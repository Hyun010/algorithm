def b_m(bin):
    a=''
    while bin>=1:
        a+=str((bin%2))
        bin=bin//2
    a=a[::-1]
    return a


def solution(n):
    answer = 0
    one_cnt=b_m(n).count('1')
    for i in range(n+1,1000001):
        if b_m(i).count('1')==one_cnt:
            answer=i
            break
    return answer