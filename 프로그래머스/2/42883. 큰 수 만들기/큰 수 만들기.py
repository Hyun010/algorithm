def solution(number, k):
    answer = []
    for i in range(len(number)):
        #answer 존재하고 제거할 것 남고, 마지막 숫자가 현재숫자보다 작으면
        while answer and k > 0 and answer[-1] < number[i]: 
            answer.pop() #큰수 만들기 위해 작은 숫자 제거
            k -= 1 #제거 숫자 낮추기
        answer.append(number[i]) #현재 숫자 추가
    
    if k > 0: #k 존재하면 뒤에서부터 잘라야 큰수
        answer = answer[:-k]
    # answer 문자열로 변환하여 반환
    answer=''.join(answer)
    return answer