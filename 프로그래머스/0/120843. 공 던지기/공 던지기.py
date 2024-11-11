def solution(numbers, k):
    answer = 0
    i=0
    cnt=0
    while cnt<k:
        answer=numbers[i%len(numbers)]
        cnt+=1
        i+=2
    return answer