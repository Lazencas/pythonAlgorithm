import sys
input = sys.stdin.readline

a1, a0 = map(int,input().split())
c = int(input())
n = int(input())

def fn(a1,a0,n):
    return (a1*n)+a0
if fn(a1,a0,n)>(c*n):
    print(0)
else:
    print(1)





