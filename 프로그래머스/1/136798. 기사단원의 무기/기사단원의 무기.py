def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        divN=0
        for j in range(1, int(i**0.5)+1):
            if i%j==0:
                divN+=2
        if i**0.5 %1==0:
            divN-=1
        if divN<=limit:
            answer+=divN
        else:
            answer+=power
    return answer