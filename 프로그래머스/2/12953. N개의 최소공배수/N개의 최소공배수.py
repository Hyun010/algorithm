def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    answer = 0
    while len(arr)>2:
        a=arr.pop()
        b=arr.pop()
        c=int(lcm(a,b))
        arr.append(c)
    answer=(lcm(arr[0],arr[1]))
    return answer