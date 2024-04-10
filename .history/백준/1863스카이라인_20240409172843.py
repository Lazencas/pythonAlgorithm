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
check = defaultdict(int)
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    build.append(y)
    
    #같은 y값 있으면 세다가 0 만나면 반환하고 초기화
    for i in build:
        print("i뭐나와",i)
        if i == 0:
            print("크기뭐나와",len(check))
            ans += len(check)
            check.clear()
        else:
            if check[i]==0:
                check[i]=1
            else:
                continue
print(ans)

