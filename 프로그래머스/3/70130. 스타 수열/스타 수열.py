from collections import Counter

def solution(a):
    if len(a) == 1: #길이가 1인 경우=>0리턴(못만든다)
        return 0 

    freq = Counter(a) #숫자 빈도별 저장
    answer = 0 
    for key in freq:
        if freq[key] * 2 <= answer: #최대길이 빠르게 구하기
            continue
        count = 0 #유효한 쌍의 개수
        i = 0 #index
        while i < len(a) - 1:
            if (a[i] == key or a[i + 1] == key) and a[i] != a[i + 1]:
                count += 1
                i += 1 #다음 요소 스킵
            i += 1 #다음 요소
        answer = max(answer, count * 2)
    return answer