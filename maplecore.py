#코어강화 경우의수
#
s1,s2,s3,s4,s5,s6 = "호밍","rm7","마그","팩","매시F","디토"

isok = True

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

s3core1 = [s3,s5,s1]
s3core2 = [s3,s6,s4]
s3list = [s3core1,s3core2]

s4core1 =[s4,s6,s1]
s4core2 = [s4,s5,s3]
s4list = [s4core1,s4core2]

s5core1 = [s5,s4,s3]
s5core2 = [s5,s3,s2]
s5core3 = [s5,s2,s4]
s5list = [s5core1,s5core2,s5core3]

s6core1 = [s6,s4,s5]
s6core2 = [s6,s2,s4]
s6core3 = [s6,s3,s1]
s6list = [s6core1,s6core2,s6core3]


#정답은 6개
combind = []
#s1~6리스트를 모두 한번씩 사용하고 ,최소 한스킬당 3번씩 들어가는 모든 조합을 모두 출력



answer = []
tempcomb= []

#3개중에 하나 골라서 반복문 돌리고  한개 카운트가 3개 넘어가면 버려야함
#여기서는 s1이런거 다 코어집합임

def corecount(s,inskill):
    if s[0]==s1 or s[1]==s1 or s[2]==s1:
        s1count += 1
    if s[0]==s2 or s[1]==s2 or s[2]==s2:
        s2count += 1
    if s[0]==s3 or s[1]==s3 or s[2]==s3:
        s3count += 1
    if s[0]==s4 or s[1]==s4 or s[2]==s4:
        s4count += 1
    if s[0]==s5 or s[1]==s5 or s[2]==s5:
        s5count += 1
    if s[0]==s6 or s[1]==s6 or s[2]==s6:
        s6count += 1
        
    return True


for s1 in s1list:
    s1count = 0
    s2count = 0
    s3count = 0
    s4count = 0
    s5count = 0
    s6count = 0
    if s1[0]==s1 or s1[1]==s1 or s1[2]==s1:
        s1count += 1
    if s1[0]==s2 or s1[1]==s2 or s1[2]==s2:
        s2count += 1
    if s1[0]==s3 or s1[1]==s3 or s1[2]==s3:
        s3count += 1
    if s1[0]==s4 or s1[1]==s4 or s1[2]==s4:
        s4count += 1
    if s1[0]==s5 or s1[1]==s5 or s1[2]==s5:
        s5count += 1
    if s1[0]==s6 or s1[1]==s6 or s1[2]==s6:
        s6count += 1
    tempcomb.append(s1)

    for s2 in s2list:
          if s1[0]==s1 or s1[1]==s1 or s1[2]==s1:
             s1count += 1
          if s1[0]==s2 or s1[1]==s2 or s1[2]==s2:
            s2count += 1
          if s1[0]==s3 or s1[1]==s3 or s1[2]==s3:
            s3count += 1
          if s1[0]==s4 or s1[1]==s4 or s1[2]==s4:
            s4count += 1
          if s1[0]==s5 or s1[1]==s5 or s1[2]==s5:
            s5count += 1
          if s1[0]==s6 or s1[1]==s6 or s1[2]==s6:
            s6count += 1
          tempcomb.append(s2)


        for s3 in s3list:
            tempcomb.append(s3)


            for s4 in s4list:
                tempcomb.append(s4)


                for s5 in s5list:
                    tempcomb.append(s5)


                    for s6 in s6list:
                        tempcomb.append(s6)
                        if 
                            answer.append(tempcomb)

print(answer)