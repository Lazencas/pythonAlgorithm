'''
시간제한2초, 256MB
S는 -100만~100만, 정수개수는 20개 이하, 주어지는 정수 -10만~10만
따로 있는 양의 수열들 구분해서 각 수열들에서 경우의 수 구해서 다 더해야겠다.

크기가 양수인 부분수열이라는 말이 이해가 잘안가서 헤맴

'''
import sys
input = sys.stdin.readline
from collections import *
from itertools import * 
def dfs(idx):
    global cnt
    #합이 S랑 같고, 크기가 0보다 크면 개수를 1개 세어준다.
    if sum(ans) == S and len(ans) > 0:
        cnt+=1
    
    #i가 0이 들어가면 다음 재귀함수 호출시 i+1인 1이 반복문에들어가고
    #이런식으로 끝까지 들어가고, pop되면서 하나 뒤로가고 거기에서 남은 반복문 실행
    #0 > 0,1 > 0,1,2 > 0,1,2,3  1 > 1,2 > 1,2,3 
    #2 > 2,3  3  이런식으로  
    for i in range(idx, N):
        ans.append(l[i])
        dfs(i+1)
        ans.pop()


plus = []
N, S = map(int,input().split())
l = list(map(int,input().split()))
cnt=0
ans=[]
dfs(0)
print(cnt)






'''
N, S = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in range(1,N+1):
    a = combinations(l,i)
    
    for j in a:
        if sum(j)==S:
            ans+=1
print(ans)
'''