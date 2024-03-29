def recur(n):
    n+=n
    if n ==1:
        return n+1
    recur(n-1)

print(recur(5))
    