def re(n):
    #1.빈리스트 만들기
    list = [0]*101

    #2.빈 리스트에 초기값 채우기
    list[1]=1
    list[2]=1
    list[3]=1
    list[4]=2
    list[5]=2
    list[6]=3
    list[7]=4
    list[8]=5
    list[9]=7
    list[10]=9
    #3.초기값과 점화식을 이용하여 리스트 채우기
    for idx in range(11,101):
        list[idx] = list[idx-1] + list[idx-5]

    #4.원하는 값 반환하기
    return list[n]

print(re(12))