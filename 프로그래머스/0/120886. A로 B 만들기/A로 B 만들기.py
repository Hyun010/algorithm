def solution(before, after):
    answer = 0
    stack=[]
    for str in before:
        stack.append(str)
    for str in after:
        if str in stack:
            stack.pop(stack.index(str))
    if stack==[]:
        answer=1
    return answer