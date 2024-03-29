# 피보나치 + n까지의합 
def recur(n):
    a = 0
    a = a+n
    if n ==1:
        return 1
    recur(n-1)

print(recur(5))
    