'''
시간제한 1초, 256MB

스티커 점수 최대값, n 10만이하
두 변을 공유하지 않는 스티커 점수의 최대값

스티커 개수가 10만개라 
자기 주변 3개 합보다 큰애는 무조건 고르고 남은거중에
자기 주변 2개 합보다 큰애
그리고 가장 큰애 순으로 집으면 됨
고른애 주변 값들은 0으로 만들어줘야 계산 편함
'''
import sys
input = sys.stdin.readline
dx=[1,0,-1,0]
dy=[0,1,0,-1]

T = int(input())
for _ in range(T):
    sticker = []
    n = int(input())
    for _ in range(2):
        dp = [list(map(int,input().split())) for _ in range(2)]
    #여기에 스티커 점수 최대값 구해서 출력하는 로직
    dp=[[0]*n for _ in range(2)]
    dp[0][1]= dp[1][0]
    dp[1][1]= dp[0][0]
    for i in range(2,n):
        dp[0][i]= max(dp[1][i-1], dp[1][i-2])
        dp[1][0]= max(dp[0][i-1], dp[0][i-2])
    print(max(dp[0][n-1], dp[1][n-1]))

