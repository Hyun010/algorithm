def solution(s):
    answer = 1 #처음 무조건 이루어짐, 분할 시 늘어남
    x=s[0] #x 처음 글자 초기화
    x_cnt=0 #x 개수
    not_cnt=0 #x아닌 개수
    for i in s:
        if x_cnt !=0 and x_cnt==not_cnt: #x개수가 0이 아니고 x와 아닌 것의 개수가 같아질때 분할
            answer+=1 #분할
            x_cnt=0 #초기화
            not_cnt=0 #초기화
            x=i #새로운 x
        if i==x: #i가 x와 같으면 x개수 업
            x_cnt+=1
        else: #다르면 아닌 개수 업
            not_cnt+=1
    return answer