import sys
a = []
answer = 0
k = int(sys.stdin.readline())
for _ in range(k):
    n = int(sys.stdin.readline())
    if n ==0 :
        a.pop()
    else:
        a.append(n)
for i in a:
    answer += i
print(answer)

