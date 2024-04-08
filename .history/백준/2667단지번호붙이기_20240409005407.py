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

def bfs(x,y):
    global cnt
    checked[x,y]=1
    queue = deque()
    if y+1<N and townmap[x][y+1] != 0:
        queue.append([x,y+1])
    elif x+1<N and townmap[x+1][y] != 0:
        queue.append([x+1,y])
    while queue:
        a, b = queue.popleft()
        if townmap[a][b]!=0:
            if checked[a,b]==0:
                checked[a,b]=1
                ans[cnt]+=1
        
        if b+1<N and townmap[a][b+1] != 0:
            queue.append([a,b+1])
        elif a+1<N and townmap[a+1][b] != 0:
            queue.append([a+1,b])
    cnt+=1

townmap = []
N = int(input())
for i in range(N):
    p = list(map(int,input().strip()))
    townmap.append(p)

cnt =0
ans=defaultdict(int)
checked = defaultdict(int)
for i in range(N):
    for j in range(N):
        if townmap[i][j]!=0:
            if checked[i,j]==0:
                bfs(i,j)

print(ans)