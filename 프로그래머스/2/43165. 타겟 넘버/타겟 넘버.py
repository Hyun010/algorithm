def solution(numbers, target):
    global answer #내부 외부에 전역변수여야 카운트 할 수 있음
    answer=0
    def dfs(i,total): #numbers를 바로 사용하기 위해 내부에 존재
        global answer #지역변수를 전역변수 처리 해주기
        if (i==len(numbers)): #마지막 탈출 조건
            if total==target:
                answer+=1
            return
        dfs(i+1,total+numbers[i]) #합계 더하기
        dfs(i+1,total-numbers[i]) #합계 빼기
        return
    dfs(0,0) #시작
    return answer