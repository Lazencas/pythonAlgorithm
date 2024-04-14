'''
시간제한 1초, 256MB
1000이하 n, 
'''
import sys
from collections import *
input = sys.stdin.readline
memo=defaultdict(int)

def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    recur(memo[n-1])
    memo[n]=memo[n-1]+memo[n-2]

    return memo[n]

n = int(input())

print(recur(n))