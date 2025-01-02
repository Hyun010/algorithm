def solution(babbling):
    valid_words = ["aya", "ye", "woo", "ma"] #발음 가능 단어
    answer = 0
    for word in babbling:
        for valid in valid_words:
            #2번이상 방지
            if valid * 2 in word:
                break
            #유효단어->공백
            word = word.replace(valid, " ")
        #결과->공백->개수증가
        if word.strip() == "":
            answer += 1
    return answer