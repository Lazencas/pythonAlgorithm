'''
2초 256MB
도시의 수 N 10이하, 각 행렬 성분은 100만 이하, 갈 수 없으면 0
모든 곳을 한번씩 돌아서 출발점으로 돌아오는데의 최소 값
결국 끝까지 가서 돌아와야 하는거니까 dfs활용 할 수 있을거 같음
bfs여도 상관 없을거 같고

각 행에서 하나씩 뽑는 경우의 수를 모두 구해서 그 합이 가장 작은 경우의 수의 합을 출력
근데 이거 도시의 수 10개 이하면, 그냥 4중 반복문 때려도 될거 같은데? -> 이건 아님

처음 시작지점에서 N-1번의 가지만큼 뻗어나가는 경우의 수
처음 고른 값의 인덱스[i][j] 에서 계산하고, 이 j값으로 이동 [j][j+1다른도시]
이런느낌

그리고 방문한 도시는 따로 처리를 해줘야함.
'''
import sys
input = sys.stdin.readline
def dfs(n,start,cost):
    global m
    if n==N-1 and distance[start][0]!=0:
        m = min(m, cost + distance[start][0])
        return
    #반복하면서 뭐가나와야지? 
    for i in range(N):
        if not visited[i] and distance[start][i]!=0:
            visited[i] = True
            dfs(n+1,i,cost+distance[start][i])
            visited[i] = False

N = int(input())
distances = []

for i in range(N):
    distance = list(map(int,input().split()))
    distances.append(distance)
visited = [False]*(N)
m = 1e9
dfs(0,0,0)
print(m)