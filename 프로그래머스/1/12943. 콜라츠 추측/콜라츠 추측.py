def solution(num):
    answer = 0
    if num==1:
        return answer
    else:
        for i in range(501):
            if num==1:
                return i
            else:
                if num%2==0:
                    num=num//2
                else:
                    num=num*3+1
        else:
            answer=-1
    return answer