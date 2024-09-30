def solution(storey):
    answer = 0
    while storey > 0: #0아래가 탈출 조건
        last_digit = storey % 10 #일의 자리
        if last_digit >= 6: #5보다 크면 +로 이동해서 10단위로 빼는게 빠름
            answer += (10 - last_digit) #10단위 맞추기위해 1의자리 이동 수
            storey += (10 - last_digit) #다음 자리수를 위해 원본에 10을 더함
        elif last_digit==5 and (storey // 10) % 10 >= 5: #5일때 동작
            answer += 5
            storey += 5
        else: #5보다 작으면 내리는게 빠름
            answer += last_digit
        storey //= 10 #10나누어 다음 자리로 이동
    return answer