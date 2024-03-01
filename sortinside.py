# 문제
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

#자리수를 나누지 않고 계산가능한가?...... 아니오
#그럼 어떻게 나누지? 문자열로 변환해서... 가아니고 입력을 문자열로 받아서 자르면 되네
N = input()
#N의 자리수를 알긴 해야하네
#N의 정수형 리스트
itgN = int(N)

#자리수 변수 numcount
numcount = 0
while itgN>0:
    itgN = itgN//10
    numcount += 1

ilist = []
answer = ''

for i in range(numcount):
    ilist.append(N[i])

#내림차순 정렬
for idx1 in range(len(ilist)-1):
    for idx2 in range(idx1+1,len(ilist)):
        if ilist[idx1] < ilist[idx2]:
            ilist[idx1], ilist[idx2] = ilist[idx2],ilist[idx1]

#리스트로 쪼개진거 다시 하나로 합치는법
#임시
for i in range(len(ilist)):
    tempstr = str(ilist[i])
    answer += tempstr

print(answer)