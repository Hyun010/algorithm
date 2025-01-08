def solution(food_times, k):
    #음식의 개수
    n = len(food_times)
    #음식이 남아있는지 확인
    if sum(food_times) <= k:
        return -1 #모든 음식을 다 먹었을 경우 -1 반환
    #음식의 남은 시간을 정렬하기 위해 인덱스와 함께 저장
    food_with_index = sorted((time, index + 1) for index, time in enumerate(food_times))
    
    total_time = 0 #총 소요된 시간
    previous_time = 0 #이전 음식의 소요 시간
    for i in range(n):
        #현재 음식의 소요 시간
        current_time = food_with_index[i][0]
        #현재 음식까지 소요된 시간 계산
        time_spent = (current_time - previous_time) * (n - i)
        #만약 k가 이 시간보다 작다면, 현재 음식에서 다시 시작
        if total_time + time_spent > k:
            #남은 음식 중 몇 번째 음식인지 찾기
            remaining_foods = sorted(food_with_index[i:], key=lambda x: x[1])
            #k에서 남은 시간만큼 빼고 남은 음식 중 다음 음식의 인덱스 반환
            return remaining_foods[(k - total_time) % (n - i)][1]
        #총 소요된 시간 업데이트
        total_time += time_spent
        previous_time = current_time #이전 시간 업데이트
    return -1 #모든 음식을 다 먹었을 경우 -1 반환