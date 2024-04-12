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
from collections import *
input = sys.stdin.readline
N = int(input())
K = int(input())
ans = 0
act = []
board = [[0]*N for _ in range(N)]
board[0][0] = 1

for _ in range(K):
    i,j = map(int,input().split())
    board[i-1][j-1] = 2

L= int(input())
for _ in range(L):
    time, direct = input().split()
    time = int(time)
    act.append([time,direct])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
nd, hx, hy = 0, 0, 0
time , i = 0,0
queue = deque()
queue.append((hx,hy))
while True:
    hx = hx + dx[nd]
    hy = hy + dy[nd]
    time+=1
    #종료조건
    if hx<0 or hx>=N or hy < 0 or hy>=N or (hx,hy) in queue:
        break
    queue.append((hx, hy))
    if board[hx][hy]==0:
        queue.popleft()
    else:
        board[hx][hy]=0
    
    if time == act[i][0]:
        if act[i][1]=='L':
            nd = (nd-1) %4

        else:
            nd = (nd+1) %4
        if i+1 < len(act):
            i+=1
print(time)