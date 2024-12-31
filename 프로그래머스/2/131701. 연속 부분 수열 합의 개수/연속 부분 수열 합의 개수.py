def solution(elements):
    sum_set=set()
    for i in range(len(elements)):
        v=elements[i]
        sum_set.add(v)
        for j in range(i+1,i+len(elements)):
            v+=elements[j%len(elements)]
            sum_set.add(v)
    return len(sum_set)