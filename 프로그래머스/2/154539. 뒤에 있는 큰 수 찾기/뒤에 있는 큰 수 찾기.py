def solution(numbers):
    answer = [-1 for _ in range(len(numbers))] #없으면 -1이라 초기값을 -1로 설정->속도 줄임
    s=[]
    for i in range(len(numbers)-1,-1,-1): #뒤에서부터 시작 가장 가까운 것을 남기기 위해, 다 통과해도 없으면 초기값인 -1
        while s and numbers[i]>=s[-1]: #스택 존재하고 현재 숫자가 스택 최근것보다 크거나 같으면 원소 삭제
            s.pop()
        if s: #최종 남은 것이 있다면
            answer[i]=s[-1] #뒷큰수 저장
        s.append(numbers[i]) #스택 쌓기
    return answer