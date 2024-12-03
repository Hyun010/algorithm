def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

def solution(number):
    answer = 0
    for n in combinations_2(number,3):
        if sum(n)==0:
            answer+=1
    return answer