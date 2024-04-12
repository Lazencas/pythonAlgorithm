'''
1초 256MB
[N-1][N-1]까지 이동, 잃는 최소금액 구하기
N 2이상 125이하

'''
import sys
input = sys.stdin.readline
N=1
n=1
while N!=0:
    N = int(input())
    cave = []
    ans = 0
    if N!=0:
        for i in range(N):            
            thief = list(map(int,input().split()))  
        cave.append(thief)
        
        print(f"Problem {n}:",ans)
        n+=1