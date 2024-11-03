def solution(array):
    answer = 0
    s=[]
    for num in array:
        for i in str(num):
            s.append(i)
    answer=s.count('7')
    return answer