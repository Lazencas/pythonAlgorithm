'''
n<=50000, 고도가 바뀌는 지점의 좌표 x,y 
1<=x<=100만, y<=50만
각 건물 경우의 수 구하는게 감도 안잡히는데, 
애초에 아래 힌트라고 써져있는거 안봣으면 문제 이해도 안됐음

언제 빌딩을 한개로 칠지가 고민
'''

import sys
from collections import *
input = sys.stdin.readline
build = []
ans = 0
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    build.append(y)

build.append(0)
stack = [0]
for j in build:
    h = j
    while stack[-1]>j:
        if stack[-1]!=h:
            ans+=1
            h=stack[-1]
        stack.pop()
    stack.append(h)
print(ans)
            
















#같은 y값 있으면 세다가 0 만나면 반환하고 초기화
#0 이전에 같은 높이여도 자기보다 낮아진 높이가 있으면 다른건물임.
#이거 더 정확하려면 그래서 내려간거 기준으로 해야할듯? > 이것도 예외있음

'''
for j in range(build):
    down = 0
    

    if build[j] == 0:
        ans += len(check)
        check.clear()
    else:
        if check[build[j]]==0:
            check[build[j]]=1
        else:
            check[build[j]]=1
ans += len(check)
print(ans)
'''
