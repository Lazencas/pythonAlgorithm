# 피보나치 + n까지의합 
def recur(n):
    if n == 1:
        return 1
    
    recur(n-1)

a= recur(5)
print(a)
    