def choice(list):
    
    for stand in range(len(list)-1):
        lowest = stand
        for idx in range(stand+1, len(list)):
            if list[lowest] > list[idx]:
                lowest = idx
        list[stand],list[lowest] = list[lowest,list[stand]
    return list

