import sys


n = int(sys.stdin.readline())
firstCar = {}
out = []
cnt = 0

# 반복문을 통해 들어간 차를 딕셔너리로 입력 받음
for i in range(n):
    firstCar[str(sys.stdin.readline().rstrip("\n"))] = i

# 반복문을 통해 나간 차를 리스트에 입력 받음
for _ in range(n):
    out.append(str(sys.stdin.readline().rstrip("\n")))

# 반복문을 통해 먼저 들어갔다 나온 차량보다 더 빨리 나온 차량이 있는지 확인
for j in range(n - 1):
    for k in range(j + 1, n):
        # 제일 먼저 나간 차의 들어간 순번 > 그 다음으로 나간 차의 들어간 순번
        print('첫번재값',firstCar[out[j]],sep='-')
        print('두번째값',firstCar[out[k]],sep='-')
        if firstCar[out[j]] > firstCar[out[k]]:
            cnt += 1
            break
print(cnt)