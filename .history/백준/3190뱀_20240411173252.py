'''
시간제한 1초, 128MB
보드 N은 100이하 N*N 

먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
만약 이동한 칸에 사과가 있다면, 
그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
즉, 몸길이는 변하지 않는다.

뱀이 움직이는함수, 사과먹엇을때 함수, 방향전환 함수?
시간초 세다가 끝났을 때 반환

뱀 이동하는 거를 어떻게 연산하지? 이동하려는 칸에 뱀이 들어가고 마지막칸에
꼬리 없애주면 될거같음
'''
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
ans = 0
act = []
board = [[0]*N for _ in range(N)]
board[0][0] = 1
snake = 1
tail_x = 0
tail_y = 0

for _ in range(K):
    i,j = map(int,input().split())
    board[i-1][j-1] = 2

L= int(input())
for _ in range(L):
    time, direct = input().split()
    time = int(time)
    act.append([time,direct])

for i in range(len(board)):
    try:
        if board[0][i+1]==2:
            board[0][i+1] = 1
            snake +=1
            ans+=1

        elif board[0][i+1] == 0:            
            board[0][i+1]=1            
            board[tail_x][tail_y]=0
            tail_y+=1
            print("tailx",tail_x,tail_y)
            ans+=1

    except:
        print('게임오버',board)


print(board)