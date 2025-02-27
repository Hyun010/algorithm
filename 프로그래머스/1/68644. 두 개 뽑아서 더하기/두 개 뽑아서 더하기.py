def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

def solution(numbers):
    answer = []
    for n in combinations_2(numbers,2):
        t=sum(n)
        if t not in answer:
            answer.append(t)
    answer.sort()
    return answer