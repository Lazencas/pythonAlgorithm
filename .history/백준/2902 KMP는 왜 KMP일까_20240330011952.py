# S = list(input().split('-'))
print(''.join(list(map(lambda x:x.upper(),[i[:1] for i in [list(input().split('-'))]]))))