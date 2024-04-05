import sys
input = sys.stdin.readline
n = int(input())
x = list(map(int,input().split()))

x2 = sorted(list(set(x)))

dic = {x2[i] : i for i in range(len(x2))}
for i in x:
    print(dic[i],end=' ')