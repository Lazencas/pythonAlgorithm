# 첫 번째 줄에 펼쳐진 카드의 개수 
# N이 주어집니다.

# 두 번째 줄부터 
# N개의 줄에 걸쳐 한 줄에 하나씩 펼쳐진 카드의 정보가 주어집니다.

# 카드의 정보는 공백으로 구분된, 과일의 종류를 나타내는 문자열 
# S와 과일의 개수를 나타내는 양의 정수 
# X로 이루어져 있습니다.

# S는 STRAWBERRY, BANANA, LIME, PLUM 중 하나입니다.
def check(fruit):
    match fruit:
        case 'STRAWBERRY':
            return 0
        case 'BANANA':
            return 1
        case 'LIME':
            return 2
        case 'PLUM':
            return 3

N = int(input())
f = ['STRAWBERRY', 'BANANA', 'LIME', 'PLUM']
c = [0,0,0,0]
for i in range(N):
    fruit, count  = input().split()
    c[check(fruit)] += count
if 5 in c:
    print('YES')
else:
    print('NO')
    
