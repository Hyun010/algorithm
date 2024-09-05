def solution(ingredient):
    answer = 0
    stack = []  # 재료를 쌓을 스택
    for item in ingredient:
        # 스택에 재료를 추가
        stack.append(item)
        # 스택의 마지막 4개 재료가 햄버거 순서(빵 - 야채 - 고기 - 빵)인지 확인
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            # 햄버거가 완성되었으므로 포장 개수를 증가
            answer += 1
            # 완성된 햄버거를 스택에서 제거
            del stack[-4:]
    return answer  # 최종 포장한 햄버거 개수를 반환