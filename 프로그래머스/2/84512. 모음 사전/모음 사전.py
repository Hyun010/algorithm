def solution(word):
    global answer #함수 안의 접근을 위한 전역변수
    answer = 0
    mo=['A','E','I','O','U'] #기본 모음
    def dfs(s):
        global answer #클로저를 위한 전역변수(함수 내부에서 외부까지 남기기 위해)
        answer+=1 #단어 인덱스
        if s==word: #단어가 워드와 동일하면, 종료조건
            return True
        if len(s)==5: #마지막 단어 5자리 확인 후 다음 모음 합치기 위한 종료조건
            return False
        for m in mo:
            if dfs(s+m)==True: #재귀 조건, 추가단어 A, AA,AAA,...
                return True
    for m in mo:
        if dfs(m)==True: #A부터 시작원하는 단어 나올때까지
            return answer