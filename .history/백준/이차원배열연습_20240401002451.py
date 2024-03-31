a = [[1,2], [4,5], [8,9]]
b = [[i]*3 for i in range(1)]

c = [list(i) for i in zip(*a)]



re = [[0]*3 for i in range(2)]
print(re)