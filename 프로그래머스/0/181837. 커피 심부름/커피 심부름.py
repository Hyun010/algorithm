def solution(order):
    answer = 0
    for str in order:
        if "cafe" in str:
            answer+=5000
        elif "ame" in  str:
            answer+=4500
        else:
            answer+=4500
    return answer