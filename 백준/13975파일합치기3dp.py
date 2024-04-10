'''
이거 1번인데 뭐하는거야;;
'''
import sys
from collections import *
from heapq import *
input = sys.stdin.readline

files = []
heapify(files)
ans = []
T = int(input())
for i in range(T):
    K = int(input())
    file = list(map(int,input().split()))
