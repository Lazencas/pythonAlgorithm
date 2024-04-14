'''
시간제한 1초, 256MB
1000이하 n, 
'''
import sys
from collections import *
input = sys.stdin.readline
memo=[]

def recur(n):
    memo=[1,2]
    for i in range(2,n):
        memo.append(memo[i-1]+memo[i-2])
    return memo[n]

n = int(input())

print(recur(n)%10007)