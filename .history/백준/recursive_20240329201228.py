# 피보나치 + n까지의합 
def recur(n):
    if n == 1:
        return 1
    
    return recur(n-1)

print(recur(5))
    