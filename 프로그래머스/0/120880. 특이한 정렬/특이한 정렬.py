def solution(numlist, n):
    answer = []
    t=[]
    t_p=[]
    t_m=[]
    order=[]
    for num in numlist:
        if num-n<0:
            t_m.append(num-n)
            t.append(num-n)
        elif num-n>=0:
            t_p.append(num-n)
            t.append(num-n)
    t_p.sort()
    t_m.sort(reverse=True)
    if t_p!=[]and t_m!=[]:
        while True:
            left=t_p[0]
            right=abs(t_m[0])
            if left<=right:
                order.append(left)
                t_p.remove(left)
            if left>right:
                order.append(t_m[0])
                t_m.remove(t_m[0])
            if t_m==[]or t_p==[]:
                break
    while True:
        if t_m!=[]:
            order.append(t_m[0])
            t_m.remove(t_m[0])
        if t_m==[]:
            break
    while True:
        if t_p!=[]:
            order.append(t_p[0])
            t_p.remove(t_p[0])
        if t_p==[]:
            break
    for num in order:
        i=t.index(num)
        answer.append(numlist[i])
    return answer