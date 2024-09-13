def solution(num_list):
    answer = 0
    e_sum=0
    o_sum=0
    for i,num in enumerate(num_list):
        if i%2==0:
            e_sum+=num
        else:
            o_sum+=num
    answer=max(o_sum,e_sum)
    return answer