'''
처음부터 순회하면서 집을 찾으면 단지1로 잡고,
해당 집이랑 붙어있는 모든 집을 찾고 complex에 찾은집을 표시한다.
덤으로 개수도 같이 세서 저장한다.> 이차원배열
다시 순환하면서 집을 찾으면 해당 집이 단지에 들어가있는 집인지 확인하고 
넘어간다.
'''
from collections import *
import sys
input = sys.stdin.readline



map = []
N = int(input())
for i in range(N):
    a = list(map(int,input().split()))
    map.append(a)

ans=[]
checked = defaultdict(int)
for i in range(N):
    for j in range(N):
        if map[i][j]!=0:
            if checked[i,j]