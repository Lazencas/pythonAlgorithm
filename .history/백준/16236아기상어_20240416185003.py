'''
2초, 512MB
자기랑 같은 물고기 칸 가고, 작으면 먹고
먹을 수 있는 물고기가 가장 가까운 칸으로 간다. 지나야 하는 칸의 최소값
거리가 가까운게 여러마리면,  가장 위, 그리고 가장 왼쪽
물고기 먹으면 빈칸, 자신의 크가와 같은 수를 먹으면 1증가

몇초 동안 물고기를 잡아먹는지
1초에 한칸 이동.

경로는 내가 정하는게 아니고 정해져 있음. 
위 조건의 경로대로 따라가고 거기에 대한 시간 초만 계산하면 됨.

문제는
먹을 수 있는 물고기가 있는 지 없는지 판단하는 함수호출 없다면 결과값 반환
최단거리 목적지 까지 이동하고 물고기 먹는 함수 호출하고
먹은 물고기 수 세서 크기 키우는 함수 호출

이러면 while문 써야 할듯 구현+좌표이동
가장 처음 아기상어 크기 2

'''

import sys
input = sys.stdin.readline
def feed_check(l):
    #먹을 수 있는 물고기가 있는지 체크
    for i in range(n):
        for j in range(n):
            if l[i][j] < shark:
                return True
    return False


n = int(input())
board = []
shark = 2
ans= 0
for i in range(n):
    a = list(map(int,input().split()))
    board.append(a)
print(board)
while True:
    if not feed_check:
        print(ans)
        break