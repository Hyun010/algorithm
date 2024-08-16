def solution(s, skip, index):
    answer = ''  # 결과 문자열을 저장할 변수
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 알파벳 목록
    
    # skip에 포함된 알파벳을 제외한 유효한 알파벳 목록 생성
    valid_alphabet = [char for char in alphabet if char not in skip]
    
    for char in s:  # 문자열 s의 각 문자에 대해
        if char in valid_alphabet:  # 문자가 유효한 알파벳인지 확인
            current_index = valid_alphabet.index(char)  # 현재 문자 인덱스 찾기
            # index만큼 뒤로 이동 (모듈로 연산을 사용하여 순환)
            new_index = (current_index + index) % len(valid_alphabet)
            answer += valid_alphabet[new_index]  # 새로운 문자 추가
        else:
            answer += char  # 유효하지 않은 문자는 그대로 추가
    
    return answer  # 최종 결과 반환