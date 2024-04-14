'''
2748 피보나치수2
1초,128MB
'''
n = int(input())
l = [0]*100
l[0]=0
l[1]=1
for i in range(2,n):
    l[i]=l[i-1]+l[i-2]

print(l[n-1])
