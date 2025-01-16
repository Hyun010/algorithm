def solution(n):
    answer = 0
    def generate_parentheses(current, open_count, close_count):
        nonlocal answer
        #현재 문자열의 길이가 n * 2이면 올바른 괄호 문자열을 찾음
        if len(current) == n * 2:
            answer += 1
            return
        #여는 괄호를 추가할 수 있는 경우
        if open_count < n:
            generate_parentheses(current + '(', open_count + 1, close_count)
        
        #닫는 괄호를 추가할 수 있는 경우
        if close_count < open_count:
            generate_parentheses(current + ')', open_count, close_count + 1)
    generate_parentheses('', 0, 0)
    return answer