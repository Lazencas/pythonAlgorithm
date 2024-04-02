board = []
for i in range(4):
    n = list(map(int,input().split()))
    board.append(n)
#지울거
print(board)
win = 0
ans = []
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] == 1:
            #흑바둑알 승리조건체크
            #가로조건체크, 세로조건체크, 대각선조건체크
            #가로조건체크부터
            tmp = [i,j]
            cnt = 0
            for a in range(j,len(board)):
                try:
                    if board[i][a]==board[i][a+1]:
                        cnt+=1
                    if cnt ==5:
                        if board[i][a]==board[i][a+1]:
                            break
                        else:
                            ans = tmp
                            win = 1

                except:break



        else:
            #흰바둑알 승리조건
            break


if win == 0:
    print(0)
else:
    print(win)
    #제일 왼쪽 바둑알 위치
