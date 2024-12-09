def solution(s):
    # 스택을 사용하여 짝지어 제거할 문자열을 저장합니다.
    stack = []

    # 문자열의 각 문자를 순회합니다.
    for char in s:
        # 스택이 비어있지 않고, 스택의 마지막 문자와 현재 문자가 같으면
        if stack and stack[-1] == char:
            # 짝을 이루므로 스택에서 제거합니다.
            stack.pop()
        else:
            # 짝이 이루어지지 않으면 스택에 현재 문자를 추가합니다.
            stack.append(char)

    # 최종적으로 스택이 비어있으면 모든 문자가 제거된 것이므로 1을 반환합니다.
    # 그렇지 않으면 0을 반환합니다.
    return 1 if not stack else 0