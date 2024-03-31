a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[i]*3 for i in range(1)]

c = [i for i in zip(*a)]
print(type(c))