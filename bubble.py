#자료개수 n개
#배열에 자료 넣고
#n-1번 반복해서 비교하는데 식  배열[0] 배열[1] 두개 비교해서 배열[0]이 더 크면 바꿈
#
#
#
#

list = [0,9,11,7,1,3,10]

def bubble(n):
    for i in range(len(n)-1):
        for idx in range(len(n)-1): 
            if n[idx] > n[idx+1]:
                n[idx], n[idx+1] = n[idx+1],n[idx]


    return print(n)



bubble(list)

klist = [0,9,11,7,1,3,10]
for a in range(len(klist)-1):
    print(klist[a])