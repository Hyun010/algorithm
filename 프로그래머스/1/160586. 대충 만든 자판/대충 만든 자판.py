def solution(keymap, targets):
    key_presses = {}  # 각 문자에 대한 입력 횟수를 저장할 딕셔너리
    answer = []  # 결과를 저장할 리스트
    # 키맵을 통해 각 문자에 대한 입력 횟수 계산
    for key in keymap:
        for press_index, char in enumerate(key):
            # 문자가 처음 등장하는 경우
            if char not in key_presses:
                key_presses[char] = press_index + 1  # 입력 횟수는 1부터 시작
            else:
                # 이미 존재하는 문자의 경우 최소 입력 횟수 업데이트
                key_presses[char] = min(key_presses[char], press_index + 1)
    # 타겟 문자열에 대해 입력 횟수 계산
    for target in targets:
        total_presses = 0  # 현재 타겟 문자열의 총 입력 횟수 초기화
        for char in target:
            if char in key_presses:
                total_presses += key_presses[char]  # 해당 문자의 입력 횟수 추가
            else:
                total_presses = -1  # 문자가 키맵에 없을 경우 -1로 설정
                break  # 더 이상 계산할 필요 없음
        answer.append(total_presses)  # 결과 리스트에 추가

    return answer  # 최종 결과 반환