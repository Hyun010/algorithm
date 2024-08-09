def solution(num_list):
    answer = 0
    hap=0
    gop=1
    for num in num_list:
        gop*=num
        hap+=num
    if gop<(hap**2):
        answer=1
    else:
        answer=0
    return answer