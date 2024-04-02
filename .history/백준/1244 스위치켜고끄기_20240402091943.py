
SC = int(input())
sl = list(map(str,input().split()))
student = int(input())

for i in range(student):
    gen, num = input().split()
    #남자일때
    if gen ==1:
        for i in range(1,len(sl)+1):
            if i%num == 0:
                if sl[i] == 0:
                    sl[i]=1
                else:
                    sl[i]=0   
