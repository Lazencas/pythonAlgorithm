'''
1초, 128MB
계단개수는 300이하, 점수는 1만이하
1.한번에 한계단 or 두계단
2.연속된 3개의 계단을 밞으면 안됨
3.마지막은 반드시 밟아야 함

최대값?
시작부터 가까운 계단 3개를 조사
그 행복유치원 사이값 이랑 비슷한 느낌인데?ㄴㄴ
조를 만드는 데 각 조에 1명~2명만 들어 가서 나오는 최대값 같음? 이것도ㄴㄴ

모든 경우의수인가? 이거 dfs로 모든 경우의 수 따지고
거기서 가장 큰 값 출력하면 되겠다.

dfs재귀로 하면 시간초과라는 걸 빠르게 캐치해야한다.
'''
import sys
from collections import *
input = sys.stdin.readline

k = int(input())
stair = [0]
for _ in range(k):
    point = int(input())
    stair.append(point)
dp = [0]*(k)

if k<=2:
    print(sum(stair))
else:
    dp[0]=stair[0]
    dp[1]=stair[0]+stair[1]
    for i in range(2,k):
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+k[i])
    print(dp[-1])
