def solution(a, b, c, d):
    dice_list=[a,b,c,d] #주사위 리스트
    dice={} #횟수를 위한 딕셔너리
    for n in dice_list:
        if n not in dice: #딕셔너리에 숫자가 없다면 추가
            dice[n]=1
        else: #있다면 횟수 증가
            dice[n]+=1
    dice=sorted(dice, key=lambda x:dice[x]) #횟수에 따라 정렬
    if len(dice)==1: #모두 같을 경우
        return 1111*a
    elif len(dice)==2: #숫자가 두개인 경우
        if dice_list.count(dice[0]) in [1,3]: # 세주사위 같은 숫자 나머지 하나 다른 숫자인 경우
            return (10*dice[1]+dice[0])**2
        else: #2개씩 같은 것
            return (dice[0]+dice[1])*abs(dice[0]-dice[1])
    elif len(dice)==3: #숫자 3개인 경우
        return dice[0]*dice[1]
    return min(dice_list) #모두 다른 경우