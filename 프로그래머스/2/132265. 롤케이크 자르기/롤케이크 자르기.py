from collections import Counter
def solution(topping):
    answer = 0
    bro1=Counter(topping) #해시테이블(딕셔너리) 종류 수
    bro2=set() #중복 제거 종류 개수만 세기 위해
    while len(bro1)>=len(bro2):
        tmp=topping.pop() #토핑 한개 뺴내기
        bro2.add(tmp) #세트에 추가
        bro1[tmp]-=1 #딕셔너리 수 제거
        if not bro1[tmp]: #토핑 개수 0이면
            del bro1[tmp] #키값 제거
        if len(bro1)==len(bro2): #토핑 종류 개수가 같으면 경우의 수 증가
            answer+=1
    return answer