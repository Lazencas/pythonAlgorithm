'''
시간제한 0.5초, 128MB

집 N개 1000이하, 모든집을 칠하는 비용의 최솟값

1번집의 색은 2번 집의 색과 같지 않아야 한다.
N번집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2<=i<=N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

인접한 집의 색이 같으면 안됨.



'''
import sys
input = sys.stdin.readline
N = int(input())
street = []
for i in range(N):
    R,G,B = map(int,input().split())
    street.append([R,G,B])
dp = [0]*N
for i in range(1,N):
    street[i][0] = min(street[i-1][1], street[i-2][2])+street[i][0]
    street[i][1] = min(street[i-1][0], street[i-2][2])+street[i][1]
    street[i][2] = min(street[i-1][0], street[i-2][1])+street[i][2]
print(min(street[N-1]))