def solution(user_id, banned_id):
    def is_valid(user, banned): #유효성 검사
        if len(user) != len(banned): #길이 다르면 유효X
            return False
        for u, b in zip(user, banned): #user와 제외 묶어서 한글자씩 비교
            if b != '*' and u != b: #한글자 *이 아니면서 같지 않으면 유효X
                return False
        return True #다 맞으면 유효O
    
    def backtrack(index, used): #목록과 인덱스로 빠르게 전체 확인하기
        if index == len(banned_id): #탈출 조건
            valid.add(tuple(sorted(used))) #중복제거(tuple) 정렬, 선택된 인덱스 추가
            return
        
        for i in range(len(user_id)):
            #선택되지 않고 검증된다면
            if i not in used and is_valid(user_id[i], banned_id[index]):
                used.add(i) #선택된 곳에 인덱스 추가
                backtrack(index + 1, used) #다음 불량자로 이동
                used.remove(i) #백트랙킹 : 인덱스 제거

    valid = set() #선택된(검증완료) 목록(중복 제거를 위한 set)
    backtrack(0, set()) #불량 아이디 인덱스와 선택된 아이디 인덱스 저장

    return len(valid)