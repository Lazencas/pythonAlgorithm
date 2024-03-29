# 피보나치 + n까지의합 
def recur(n):
    print(n)
    if n == 1:
        return 1
    recur(n-1)
    return 

print(recur(5))
    