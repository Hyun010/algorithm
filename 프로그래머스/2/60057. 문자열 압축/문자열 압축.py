def solution(s):
    length = len(s) #길이
    answer = length+1 #최대값으로 초기화
    if length == 1:
        return 1
    for unit in range(1, length // 2 + 1): #단위 길이 설정
        compressed = "" #압축된 문자열
        count = 1 #반복 문자열개수
        for i in range(0, length, unit): #압축(단위 길이별)
            if s[i:i + unit] == s[i + unit:i + 2 * unit]: #비교
                count += 1 #문자열 반복->카운트 증가
            else:
                #압축 문자열 만들기
                compressed += (str(count) if count > 1 else "") + s[i:i + unit]
                count = 1 #초기화
        answer = min(answer, len(compressed)) #최소 문자열 길이
    return answer