def solution(n):
    answer = ''
    temp=[]
    for num in str(n):
        temp.append(num)
    temp.sort(reverse=True)
    for num in temp:
        answer+=num
    return int(answer)