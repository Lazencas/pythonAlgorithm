def recur(n):
    a=0
    a+=n
    if n ==1:
        return a+1
    recur(n-1)

print(recur(5))
        
    