'''
시간제한 1초, 256MB
1000이하 n, 
'''
import sys
from collections import *
input = sys.stdin.readline
memo = {}
def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    
    memo[n]= recur(n-1) + recur(n-2)
    return memo[n]
    
n = int(input())

print(recur(n)%10007)