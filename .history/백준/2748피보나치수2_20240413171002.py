'''
2748 피보나치수2
1초,128MB
'''
n = int(input())
l = [0]*n+1
l[0]=0
l[1]=1
for i in range(2,n+1):
    l[i]=l[i-1]+l[i-2]

print(l[n])
