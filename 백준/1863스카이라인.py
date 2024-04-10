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

sky = []
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    sky.append(y)

#스택에 넣으면서 값이 현재 값보다 작아지는 순간, 스택에서 지금까지 있던
#건물 개수 세는거
ans = 0
sky.append(0)
stack = [0]
for i in sky:
    preh = i
    #새로 뽑은애가, 스택의 마지막 값보다 작아지면, 건물 개수세야함
    while stack[-1]>i:
        #그리고 preh랑 값이 달라야함
        if stack[-1] != preh:
            ans+=1
            preh = stack[-1]
        stack.pop()

    #새로 뽑은애가 스택의 마지막 값보다 커지면, 스택 추가
    stack.append(i)
















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
