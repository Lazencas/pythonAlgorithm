'''
시간제한 1초, 256MB

'''
import sys
input = sys.stdin.readline
n = int(input())
dp = [0]*1001
dp[1]=1
dp[2]=3
if n==1:
    print(1)
else:
    for i in range(3,n+1):
        dp[i]=(dp[i-1] + dp[i-2] *2)%10007
    print(dp[n])