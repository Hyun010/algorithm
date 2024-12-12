def solution(food):
    answer = ''
    for idx,i in enumerate(food):
        if i>=2:
            cnt=i//2
            answer+=str(idx)*cnt
    temp=answer[::-1]
    answer=answer+'0'+temp
    return answer