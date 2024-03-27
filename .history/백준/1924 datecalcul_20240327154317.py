# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
def caldate(date):
    if date==1 or date==3 or date==5 or date==7 or date==8 or date==10 or date==12:
        return 31
    else:
        return 0

M, D = input().split(' ')
M = int(M)
date = 0
for i in range(1,M):
    print(caldate(i))

    