def solution(s):
    answer = []
    for string in s:
        stack = []
        counting = 0
        #110 제거
        for st in string:
            if(len(stack) >= 2 and stack[-1] == '1' and stack[-2] =='1' and st =='0'):
                counting+=1
                stack.pop()
                stack.pop()
            else:
                stack.append(st)
        count_1 = 0
        #1개수 확인
        for st in stack[::-1]:
            if st == '0':
                break
            else:
                count_1 += 1
        answer.append(''.join(stack[:len(stack)-count_1])+(counting)*'110'+count_1*'1')
    return answer