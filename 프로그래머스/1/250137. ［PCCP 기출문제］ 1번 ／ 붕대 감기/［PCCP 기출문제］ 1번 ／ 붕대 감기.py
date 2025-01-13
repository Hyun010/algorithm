def solution(bandage, health, attacks):
    t, x, y = bandage #정보 파싱
    max_health = health  #최대 체력
    current_health = health #현재 체력
    success_time = 0 #연속 성공 시간
    attack_index = 0 #현재 공격 인덱스
    attack_count = len(attacks) #공격 횟수

    #최대 시간 1000초 동안 시뮬레이션
    for current_time in range(1, 1001):
        #공격 시간이 일치하면 처리
        if attack_index < attack_count and attacks[attack_index][0] == current_time:
            damage = attacks[attack_index][1]
            current_health -= damage  # 체력 감소
            success_time = 0 #연속 성공 초기화
            attack_index += 1 #다음 공격으로 이동

            #체력이 0 이하라면 즉시 종료
            if current_health <= 0:
                return -1
        #공격 시간이 아닐 경우 회복 처리
        else:
            if success_time < t: #연속 회복 중
                current_health += x
                success_time += 1
                #최대 체력 초과 방지
                current_health = min(current_health, max_health)
            if success_time == t: #연속 성공 시간 도달
                current_health += y #추가 회복량
                #최대 체력 초과 방지
                current_health = min(current_health, max_health) 
                success_time = 0 #연속 성공 초기화
        #공격이 끝났다면 반복 종료
        if attack_index >= attack_count:
            break
    return current_health