a = [1,2,3,4,5]
n = int(input())
for i in range(len(a)):
    try:
        if (i+1) == n:
            a[i+1]=0
    except:
        break

print(a)