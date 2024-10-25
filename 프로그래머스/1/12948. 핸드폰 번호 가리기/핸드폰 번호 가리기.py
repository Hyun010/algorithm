def solution(phone_number):
    answer = ''
    phone_number=phone_number[::-1]
    for i,num in enumerate(phone_number):
        if i<4:
            answer+=num
        else:
            answer+='*'
    answer=answer[::-1]
    return answer