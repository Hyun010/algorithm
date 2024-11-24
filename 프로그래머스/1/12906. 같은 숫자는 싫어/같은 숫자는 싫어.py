def solution(arr):
    answer = []
    t=-1
    for num in arr:
        if t<0:
            t=num
            answer.append(num)
        else:
            if t==num:
                pass
            else:
                t=num
                answer.append(num)
    return answer