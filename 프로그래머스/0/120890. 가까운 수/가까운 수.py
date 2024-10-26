def solution(array, n):
    answer = 0
    s=[]
    ma=-101
    mi=101
    idx_ma=0
    idx_mi=0
    for num in array:
        s.append(num-n)
    for i,num in enumerate(s):
        if num==0:
            answer=array[i]
            break
        else:
            if num<0:
                if num>ma:
                    ma=num
                    idx_ma=i
                else:
                    continue
            else:
                if num<mi:
                    mi=num
                    idx_mi=i
                else:
                    continue
    if answer==0:
        if abs(ma)==abs(mi):
            answer=array[idx_ma]
        elif abs(ma)>abs(mi):
            answer=array[idx_mi]
        else:
            answer=array[idx_ma]
    return answer