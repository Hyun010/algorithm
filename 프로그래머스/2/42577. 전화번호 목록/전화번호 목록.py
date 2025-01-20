def solution(phone_book):
    answer = True
    phone_book.sort() # 접두어면 인접하게 배치
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            answer=False
            break
    return answer