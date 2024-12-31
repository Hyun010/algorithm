import sys
sys.setrecursionlimit(100000)

def solution(k, room_number):
    rooms = {} #방 상태
    #방 번호 찾기(경로압축)
    def find(room):
        if room not in rooms:
            rooms[room] = room #방 빔->자기 자신을 부모 설정
            return room
        if rooms[room] != room:
            rooms[room] = find(rooms[room]) #경로 압축
        return rooms[room]
    answer = []
    for request in room_number:
        #요청한 방의 루트를 찾음
        available_room = find(request)
        answer.append(available_room)
        #배정된 방의 다음 방 번호를 업데이트
        rooms[available_room] = find(available_room + 1)
    return answer