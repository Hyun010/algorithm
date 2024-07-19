def solution(dirs):
    answer = 0
    load=set() #길 중복 제거
    x,y=0,0 #초기 위치
    move={'U':(1,0),'D':(-1,0),'R':(0,1),'L':(0,-1)} #이동 명령어(실제 좌표이동)
    for d in dirs: #방향대로 이동
        dx,dy=move[d] #이동 방향 좌표 설정
        ny=y+dy #좌표이동
        nx=x+dx #좌표이동
        if -5<=ny<=5 and -5<=nx<=5: #경계면 조건 안에 존재하면
            #총 경로의 개수는 방향성이 없기 때문에 시작-끝, 끝과 시작으로 2개가 된다
            load.add(((y,x),(ny,nx))) #시작과 끝 하나의 길
            load.add(((ny,nx),(y,x))) #끝과 시작 하나의 길
            y=ny #이동한 좌표로 y 설정
            x=nx #이동한 좌표로 x 설정
    answer=len(load)//2 #처음가는 길*2가 된 상태라서 //2로 실제 처음가는길을 구한다
    return answer