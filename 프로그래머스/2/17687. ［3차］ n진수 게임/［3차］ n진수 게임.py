def convert_num(num,d): #진수 바꾸기
    base='0123456789ABCDEF' #기본 베이스(최대 16진수)
    q,r=divmod(num,d) #들어온 숫자를 진법에 맞게 몫과 나머지
    
    if q==0: #10진법 아래
        return base[r] #0~9까지 표현
    else:
        return convert_num(q,d)+base[r] #진법에 맞춰 표현

def solution(n, t, m, p):
    answer = ''
    num=0 #0부터 시작
    while True:
        answer+=convert_num(num,n) #n진법으로 나타낸 수
        if len(answer)>=t*m: #최대 숫자 t*m이 되면 탈출 조건
            answer=answer[:t*m]
            return answer[p-1:t*m:m] #순서 시작(p-1)부터 t*m 끝까지 m사람수 만큼 증가하는 조건으로 슬라이싱하면 튜브 문자열
        num+=1 #수 증가
    return answer