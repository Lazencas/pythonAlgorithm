import sys
integer = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split(' ')))
v = int(sys.stdin.readline())
count = 0
for i in a:
    if v == i:
        count+=1
print(count)