def solution(numbers):
    max=-1000000000
    for i in range(0,len(numbers)-1):
        for j in range(1,len(numbers)):
            if i!=j:
                m=numbers[i]*numbers[j]
                if max<m:
                    max=m
    return max