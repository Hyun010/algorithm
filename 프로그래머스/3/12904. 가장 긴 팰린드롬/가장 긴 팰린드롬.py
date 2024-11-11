def solution(s):
    answer = 0
    n = len(s) #문자열 길이
    for center in range(n):
        #홀수 길이
        left, right = center, center
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1
        #짝수 길이
        left, right = center, center + 1
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1
    return answer