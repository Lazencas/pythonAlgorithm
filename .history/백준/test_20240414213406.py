def selection_sort(l):
    for stand in range(len(l)):
        lowest = stand
        for i in range(stand+1,len(l)):
            if l[i]<l[lowest]:
                lowest = i
        l[stand], l[lowest] = l[lowest], l[stand]
    
    return l


a = [40, 1, 5, 74, 24, 56, 30, 99, 7]
print(selection_sort(a))