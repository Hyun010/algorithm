import math
def solution(num1, num2):
    answer = 0
    if(0<=num1<=100 and 0<=num2<=100):
        answer=math.trunc(num1/num2*1000)
    return answer