def solution(n, s):
    if n>s: #합이 개수보다 작으면 구할 수 없다
        return[-1]
    q,r=s//n,s%n #곱이 최대가 되기 위한 조건이 평균에 가깝다
    answer=[q]*n #답 리스트 생성
    for i in range(r): #나머지 더하기
        answer[i]+=1
    return sorted(answer) #오름차순 정렬