'''
시간제한 1초, 256MB
1000이하 n, 
'''
import sys
input = sys.stdin.readline
def recur(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    return recur(n-2)+recur(n-1)

n = int(input())
print(recur(n))