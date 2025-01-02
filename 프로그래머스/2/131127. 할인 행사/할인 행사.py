def solution(want, number, discount):
    answer = 0
    n=len(discount)
    rd=0
    while rd+10<=n:
        ok_day=discount[rd:rd+10]
        if all(num==ok_day.count(product) for product, num in zip(want,number)):
            answer+=1
        rd+=1
    return answer