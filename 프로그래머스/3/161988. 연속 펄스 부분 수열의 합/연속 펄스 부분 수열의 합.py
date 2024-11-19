#펄스 수열 생성
def generate_psequence(l, s):
    return [s if i % 2 == 0 else -s for i in range(l)]

#수열 합 계산
def max_sums(arr):
    max_sum = float('-inf')
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

def solution(sequence):
    psequence1 = generate_psequence(len(sequence), 1) #1로 시작 펄스
    psequence2 = generate_psequence(len(sequence), -1) #-1로 시작 펄스
    #펄스와 곱
    tsequence1 = [sequence[i] * psequence1[i] for i in range(len(sequence))]
    tsequence2 = [sequence[i] * psequence2[i] for i in range(len(sequence))]
    #수열 합
    max_sum1 = max_sums(tsequence1)
    max_sum2 = max_sums(tsequence2)
    return max(max_sum1, max_sum2)
