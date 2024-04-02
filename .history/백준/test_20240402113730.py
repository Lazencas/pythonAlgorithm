a = [1,2,3,4,5]

for i in range(len(a)):
    try:a[i+1]=0
    except:break
print(a)