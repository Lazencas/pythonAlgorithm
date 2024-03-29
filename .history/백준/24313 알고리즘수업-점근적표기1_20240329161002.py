import sys
input = sys.stdin.readline

a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())
answer = 1
def fn(a1,a0,n0):
    return (a1*n0)+a0
for i in range(n0,10001):    
    if fn(a1,a0,i)<=(c*i):
        answer = 0
        break
print(answer)






