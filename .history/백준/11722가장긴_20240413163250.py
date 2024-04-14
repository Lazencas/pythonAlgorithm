'''
시간제한1초, 256MB
N은 1000이하, 
가장 긴 감소하는 수열의 길이.
점점 줄어드는 숫자가 최대 몇개인지
dp는 답이 없는데
'''
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))

dp = [0]*1001

for i in range(N):
    for j in range(0,i):
        if A[i]<A[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))