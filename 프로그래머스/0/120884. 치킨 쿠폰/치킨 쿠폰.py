def solution(chicken):
    answer = 0
    extra=0
    while True:
        answer+=chicken//10
        c=chicken//10
        extra+=chicken-(c*10)
        chicken//=10
        if extra>=10:
            answer+=1
            chicken+=1
            extra-=10
        if chicken<10:
            break
    if chicken+extra>=10:
        answer+=1
    return answer