
SC = int(input())
sl = list(map(int,input().split()))
student = int(input())
for i in range(student):
    gen, num =map(int,input().split())
    #남자일때
    if gen == 1:
        for i in range(0,len(sl)):
            if (i+1)%num == 0:
                if sl[i] == 0:
                    sl[i]=1
                else:
                    sl[i]=0   
    #여자일때
    else:
        for i in range(0,len(sl)//2):
            if (i+1) == num:
                if sl[i] == 0:
                    sl[i]=1
                else:
                    sl[i]=0
                #대칭로직?
                if SC < (num-1)+i or (num-1)-i <0 :
                    break
                if sl[(num-1)+i] == sl[(num-1)-i]:
                    if sl[(num-1)+i] == 0:
                        sl[(num-1)+i]=1
                    else:
                        sl[(num-1)+i]=0
                    
                    if sl[(num-1)-i] == 0:
                        sl[(num-1)-i]=1
                    else:
                        sl[(num-1)-i]=0
                else:
                    break
for i in range(len(sl)):
    print(sl[i],end=' ')
    if i !=0:
        if i % 20 == 0:
            print()
