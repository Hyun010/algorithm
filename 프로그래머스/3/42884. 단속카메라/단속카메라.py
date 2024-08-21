def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 차량의 진출 지점으로 정렬(최소 조건)
    print(routes)
    last_camera_position = -30001  #마지막으로 설치한 카메라의 위치, -30,000보다 작게 초기화
    for route in routes:
        if route[0] > last_camera_position: # 현재 차량의 진출 지점이 마지막 카메라 위치보다 크면
            answer += 1  # 카메라 수 증가
            last_camera_position = route[1]  # 현재 차량의 진출 지점에 카메라 설치
    return answer  # 설치한 카메라 수 반환