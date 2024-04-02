
SC = int(input())
sl = list(map(str,input().split()))
student = int(input())
print(sl)
for i in range(student):
    gen, num =map(int,input().split())
    #남자일때
    if gen == 1:
        for i in range(0,len(sl)):
            if (i+1)%num == 0:
                if sl[i] == '0':
                    sl[i]=1
                else:
                    sl[i]=0   
    #여자일때
    else:
        l=0
        for i in range(0,len(sl)//2):
            if (i+1) == num:
                #대칭로직?
                if SC < num+i or num-i <0 :
                    break
                if sl[num+i] == sl[num-i]:
                    if (i+1)%num == 0:
                        if sl[i] == '0':
                            sl[i]=1
                        else:
                            sl[i]=0
print(sl)
