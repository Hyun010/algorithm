def solution(a, b):
    answer = ''
    mday=0
    days=0
    check_w=['FRI','SAT','SUN','MON','TUE','WED','THU'] #1월 1일부터 시작하는 요일 반복
    for i in range(1,a): #월수 만큼 반복해서 찾을 것이다
        if i%2 != 0 and i<=7: #후반기 31일 있는 달 1 3 5 7
            mday=31
        elif i ==2 : #윤달 2
            mday=29
        elif i%2==0 and i>7: #상반기 31일 있는달 8 10
            mday=31
        else: #나머지 30일 있는 달 4 6 9
            mday=30
        days+=mday #원하는 날짜까지 걸리는 일수 구하기
    days+=b
    answer=check_w[(days%7)-1]
    return answer