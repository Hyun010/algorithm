from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words: #목표 단어가 words에 없을 경우 빠르게 리턴
        return answer
    def bfs(begin, target, words):
        q=deque() #큐 생성
        q.append([begin,0]) #시작 단어 단계0 초기화
        while q:
            now, answer=q.popleft() #현재 단어와 현재 변화 과정
            if now == target: #현재 단어가 타겟이면 단계 출력
                return answer
            for w in words:
                cnt=0 #단어가 다른 경우의 수를 알기 위한 변수
                for i in range(len(now)): #단어 길이만큼 반복하면서
                    if now[i] !=w[i]: #알파벳 한개씩 체크
                        cnt+=1
                if cnt==1: #조건에 부합(1개만 변경가능)
                    q.append([w,answer+1]) #다음 스텝으로 넘어가 확인한다
    return bfs(begin,target,words)