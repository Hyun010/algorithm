import heapq

def solution(book_time):
    answer=0
    times = [] #시간 리스트
    for s, e in book_time:
        start_h, start_m = map(int, s.split(':'))
        end_h, end_m = map(int, e.split(':'))
        #분 단위로 변환, 끝은 청소시간 추가
        times.append((start_h * 60 + start_m, end_h * 60 + end_m + 10))
    times.sort() #시작 기준 정렬
    rooms = []
    for s, e in times:
        # 종료 시간이 시작 시간보다 작거나 같으면 방을 재사용 가능
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms) #방 재사용
        heapq.heappush(rooms, e) #새손님 방 추가
    # 필요한 방의 수를 반환
    return len(rooms)