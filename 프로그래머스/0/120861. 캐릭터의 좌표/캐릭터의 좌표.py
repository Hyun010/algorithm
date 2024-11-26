def solution(keyinput, board):
    answer = []
    x=0
    y=0
    for key in keyinput:
        if key=='left' or key=='right':
            if x>=-(board[0]//2) and x<=(board[0]//2):
                if key=='left':
                    if x==-(board[0]//2):
                        x=x
                    else:
                        x-=1
                else:
                    if x==(board[0]//2):
                        x=x
                    else:
                        x+=1
            else:
                x=x  
        else:
            if y>=-(board[1]//2) and y<=(board[1]//2):
                if key=='down':
                    if y==-(board[1]//2):
                        y=y
                    else:
                        y-=1
                else:
                    if y==(board[1]//2):
                        y=y
                    else:
                        y+=1
            else:
                y=y
    answer.append(x)
    answer.append(y)
    return answer