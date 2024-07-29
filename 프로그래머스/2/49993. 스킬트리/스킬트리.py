def solution(skill, skill_trees):
    answer=0 #스킬트리 개수
    s=[] #
    for k in skill_trees: #스킬트리중 선행스킬 있는지 파악
        str1='' #선행스킬트리 묶는 문자열
        for i in k: #한글자씩 파악
            if i in skill: #선행스킬이면
                str1+=i #선행스킬트리 문자열에 증가
            else: #선행스킬이 아니면 패스
                continue
        s.append(str1) #스택에 선행스킬을 추가
    for i in s: #스택중 선행스킬들 확인
        if skill[:len(i)]==i: #선행스킬 순서가 맞으면 통과
            answer+=1 #증가
        else: #아니면
            continue #패스
    return answer