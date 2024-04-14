'''
시간제한 1초, 256MB
1000이하 n, 
'''
import sys
input = sys.stdin.readline
memo={}
def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    memo[n]=memo[n-1]+memo[n-2]

    return memo[n]

n = int(input())

print(recur(n))