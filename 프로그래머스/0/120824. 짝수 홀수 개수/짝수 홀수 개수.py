def solution(num_list):
    answer = []
    cnt_even=0
    cnt_odd=0
    for num in num_list:
        if num%2==0:
            cnt_even+=1
        else:
            cnt_odd+=1
    answer=[cnt_even,cnt_odd]
    return answer