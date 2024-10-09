def split_uv(p): #균형잡힌 괄호 문자열 u,v 나누기
    balance = 0
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0: #균형->u,v 리턴
            return p[:i + 1], p[i + 1:]

def is_correct(u): #u->올바른 괄호 문자열 확인
    balance = 0
    for char in u:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0: #중간 음수면 올바르지 않음
            return False
    return balance == 0 #통과후 밸런스면 올바른 괄호
        
def solution(p):
    if not p: #빈 문자열
        return ""
    u, v = split_uv(p)
    if is_correct(u): #u 올바른 문자열
        return u + solution(v) #재귀열로 뒤에 확인 후 이어 붙이기
    else:
        new_v = '(' + solution(v) + ')' #(붙이고 재귀적 v, )붙이기
        new_u = ''.join(')' if char == '(' else '(' for char in u[1:-1]) #u의 첫,마지막 제거 후 나머지 문자열 괄호 방향 반대로
        return new_v + new_u