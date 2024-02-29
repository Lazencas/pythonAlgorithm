from collections import *
#코어강화 경우의수
#
s1,s2,s3,s4,s5,s6 = "호밍","rm7","마그","팩","매시F","디토"



inskill = [s1,s2,s3,s4,s5,s6]

s1core1 = [s1,s6,s2]
s1core2 = [s1,s3,s5]
s1core3 = [s1,s4,s6]
s1list = [s1core1,s1core2,s1core3]

s2core1 = [s2,s1,s3]
s2core2 = [s2,s1,s6]
s2core3 = [s2,s1,s4]
s2core4 = [s2,s5,s6]
s2list = [s2core1,s2core2,s2core3,s2core4]
# s2list = [s2core1]

s3core1 = [s3,s5,s1]
s3core2 = [s3,s6,s4]
s3list = [s3core1,s3core2]
# s3list = [s3core1]

s4core1 =[s4,s6,s1]
s4core2 = [s4,s5,s3]
s4list = [s4core1,s4core2]
# s4list = [s4core1]

s5core1 = [s5,s4,s3]
s5core2 = [s5,s3,s2]
s5core3 = [s5,s2,s4]
s5list = [s5core1,s5core2,s5core3]
# s5list = [s5core1]

s6core1 = [s6,s4,s5]
s6core2 = [s6,s2,s4]
s6core3 = [s6,s3,s1]
s6list = [s6core1,s6core2,s6core3]
# s6list = [s6core1]

#각 스킬의 카운트 변수
skillcount = [0,0,0,0,0,0]

answer =[]
temp = []
N = 3
isok = True

#이 함수 이용해서 카운트 하는데, 리턴값 숫자로 받자
#11,22,33,44,55,66?
#딕셔너리 이용하자 < 쓸 이유가 없음 그냥 배열 쓰는게 접근하기 편함
def scount(slist):
    if slist[0]==s1 or slist[1]==s1 or slist[2]==s1:
        skillcount[0]+=1
    if slist[0]==s2 or slist[1]==s2 or slist[2]==s2:
        skillcount[1]+=1
    if slist[0]==s3 or slist[1]==s3 or slist[2]==s3:
        skillcount[2]+=1
    if slist[0]==s4 or slist[1]==s4 or slist[2]==s4:
        skillcount[3]+=1
    if slist[0]==s5 or slist[1]==s5 or slist[2]==s5:
        skillcount[4]+=1
    if slist[0]==s6 or slist[1]==s6 or slist[2]==s6:
        skillcount[5]+=1

#scount함수로 올린거 롤백하는기능의 함수
def scountrollback(slist):
    if slist[0]==s1 or slist[1]==s1 or slist[2]==s1:
        skillcount[0]-=1
    if slist[0]==s2 or slist[1]==s2 or slist[2]==s2:
        skillcount[1]-=1
    if slist[0]==s3 or slist[1]==s3 or slist[2]==s3:
        skillcount[2]-=1
    if slist[0]==s4 or slist[1]==s4 or slist[2]==s4:
        skillcount[3]-=1
    if slist[0]==s5 or slist[1]==s5 or slist[2]==s5:
        skillcount[4]-=1
    if slist[0]==s6 or slist[1]==s6 or slist[2]==s6:
        skillcount[5]-=1

#스킬이 입력한 N보다 큰지 확인하는 함수
def scheck(skillcount):
    for s in skillcount:
        if s > N:
            return False
    return True

#마지막으로 스킬이 입력한 N보다 작은지 확인하는 함수
def scheckfinal(skillcount):
    for s in skillcount:
        if s < N:
            return False
    return True

#스킬카운트 리셋함수
def countreset(skillcount):
    skillcount[0]=0
    skillcount[1]=0
    skillcount[2]=0
    skillcount[3]=0
    skillcount[4]=0
    skillcount[5]=0

#문제정의
#코어M, 중첩수N을 입력받으면
#s1~6리스트를 모두 한번씩 사용하고 < 이건 6중반복문쓰고 ,한스킬당 N번씩 들어가는 모든 조합을 모두 출력
#N번들어가 있는지 체크하는 방법?
#각 0번 1번 2번 인덱스를 꺼내서 6개의 스킬과 비교하고 같으면 카운트 올리는식으로 
#카운트가 N번을 넘으면 안되고, 마지막에 끝날때 N번 이하인게 있어도 안됨
#정답 자료구조 어케하지?
#s1core2, s2core1, s3core2 이런식으로 답나오게 or 

#숫자 뽑아서 정답리스트에 넣고, 숫자 카운
#컨티뉴하고 완전 다음으로 건너가면 스킬카운트가 리셋이안됨
#컨티뉴문 빼고 isok로 마지막만 체크하자
for ss1 in s1list:
    temp = []
    countreset(skillcount)
    scount(ss1)
    temp.append(ss1)

    for ss2 in s2list:
        scount(ss2)
        temp.append(ss2)

        for ss3 in s3list:
            scount(ss3)
            temp.append(ss3)
            isok = scheck(skillcount)

            for ss4 in s4list:
                scount(ss4)
                temp.append(ss4)
                isok = scheck(skillcount)

                for ss5 in s5list:
                    scount(ss5)
                    temp.append(ss5)
                    isok = scheck(skillcount)

                    for ss6 in s6list:
                        scount(ss6)
                        temp.append(ss6)
                        isok = scheck(skillcount)
                        isok = scheckfinal(skillcount)

                        if isok:
                            answer.append(temp)
                        
                        temp = []
                        countreset(skillcount)


                        
                        
#템프랑 스킬카운트 초기화를 어케해야하지?
print(answer)