def solution(x):
    answer = True
    numli=[]
    for num in str(x):
        numli.append(int(num))
    sumli=sum(numli)
    if x%sumli!=0:
        answer=False
    return answer