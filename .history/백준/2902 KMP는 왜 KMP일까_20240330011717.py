S = list(input().split('-'))
p = list(map(lambda x:x.upper(),[i[:1] for i in S]))
print(''.join(p))