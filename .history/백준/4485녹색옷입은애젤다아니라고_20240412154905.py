'''
1초 256MB
[N-1][N-1]까지 이동, 잃는 최소금액 구하기
N 2이상 125이하 N최대 크기 125*125

이것도 다익스트라 맞는거 같다. 똑같은 크기의 판을 만들고
해당 칸에 최소 값을 넣어주는 식으로 하면 될거같은데, 시작인 자기자신은 값 고정.
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
        #여기부터 얻는 값이 최소가 되는 루트를 산출하는 로직
        #[0][0]번시작이니 해당 칸의 값은 일단 가지고 시작~[-1][-1]까지
        new_cave = [[100000]*N for _ in range(N)]
        new_cave[0][0] = cave[0][0]
        print(new_cave)


        print(f"Problem {n}:",ans)
        n+=1