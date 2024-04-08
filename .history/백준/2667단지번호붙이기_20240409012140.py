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
    cnt = 0
    checked[x,y]=1
    queue = deque()
    queue.append([x,y])
    cnt+=1

    while queue:
        a, b = queue.popleft()
        if b+1<N and townmap[a][b+1] != 0:
            if townmap[a][b]!=0:
                if checked[a,b]==0:
                    checked[a,b]=1
                    cnt+=1
                    queue.append([a,b+1])
        elif a+1<N and townmap[a+1][b] != 0:
            if townmap[a][b]!=0:
                if checked[a,b]==0:
                    checked[a,b]=1
                    cnt+=1
                    queue.append([a+1,b])
        elif N<a-1 and townmap[a-1][b]!=0:
            if townmap[a][b]!=0:
                if checked[a,b]==0:
                    checked[a,b]=1
                    cnt+=1
                    queue.append([a-1,b])
        elif N<b-1 and townmap[a][b-1]!=0:
            if townmap[a][b]!=0:
                if checked[a,b]==0:
                    checked[a,b]=1
                    cnt+=1
                    queue.append([a,b-1])
    
    return cnt

townmap = []
N = int(input())
for i in range(N):
    p = list(map(int,input().strip()))
    townmap.append(p)

cnt = []
ans=defaultdict(int)
checked = defaultdict(int)
for i in range(N):
    for j in range(N):
        if townmap[i][j]!=0:
            if checked[i,j]==0:
                cnt.append(bfs(i,j))

print(cnt)