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
'''
import sys
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

for i in range(len(board)):
    for j in range(len(board)):
        board[10][10]