'''
시간제한 1초, 256MB
1000이하 n, 
'''
import sys
from collections import *
input = sys.stdin.readline

def recur(n):
    memo=[1,2]
    for i in range(2,n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n-1]

n = int(input())

print(recur(n)%10007)