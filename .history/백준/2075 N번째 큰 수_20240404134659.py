'''

'''
import sys
input = sys.stdin.readline
n_list=[]
n = int(input())
for i in range(n):
    a = list(map(int,(input().split())))
    n_list.append(a)
print(n_list)    
