for index in range(데이터길이-1):
    for index2 in range(index+1,0,-1):
        if data[index2] < data[index]:
            swap(data[index2],data[index2-1])
        else:
            break