def solution(numbers):
    def can_form_tree(binary_str):
        """ 주어진 이진 문자열이 포화 이진트리 구조를 가질 수 있는지 확인 """
        n = len(binary_str)
        root_idx = n // 2 #루트노드 가운데 인덱스
        root = binary_str[root_idx] #루트노드
        #루트=0->자식 1=>불가능
        if root == '0' and '1' in binary_str:
            return False
        #길이가 1=>바로 가능
        if n == 1:
            return True
        #왼쪽 서브트리와 오른쪽 서브트리 확인(재귀)
        return can_form_tree(binary_str[:root_idx]) and can_form_tree(binary_str[root_idx+1:])
    
    def get_full_binary(num):
        """ 숫자를 이진수로 변환하고 포화 이진트리 형태로 변환 """
        binary_str = bin(num)[2:] #숫자를 이진수로 변환(앞 '0b' 제거)
        #포화 이진트리를 만족하는 길이 찾기 (2^h - 1 꼴)
        length = 1
        while length < len(binary_str):
            length = length * 2 + 1
        #앞쪽에 '0'을 추가하여 포화 이진트리 형태 맞추기
        return binary_str.zfill(length)
    answer = []
    for num in numbers:
        full_binary = get_full_binary(num)
        answer.append(1 if can_form_tree(full_binary) else 0)
    return answer