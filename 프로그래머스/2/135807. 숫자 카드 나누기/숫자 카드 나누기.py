from functools import reduce

#최대공약수(GCD)
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

#GCD로 나눌 수 있는지 확인
def can_divide(gcd, array):
    return all(num % gcd != 0 for num in array) #모두 통과하면 True

#모든 원소 GCD계산
def array_gcd(arr):
    return reduce(gcd, arr)

def solution(arrayA, arrayB):
    answer = 0
    gcdA = array_gcd(arrayA) #철수 GCD
    gcdB = array_gcd(arrayB) #영희 GCD
    if can_divide(gcdA, arrayB): #철수 GCD->영희것들 나누기X->최대값
        answer = gcdA
    if can_divide(gcdB, arrayA): #영희 GCD->철수것들 나누기X->최대값
        answer = max(answer, gcdB)
    return answer