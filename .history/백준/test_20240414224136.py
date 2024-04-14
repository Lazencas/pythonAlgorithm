def selection_sort(l):
    for stand in range(len(l)):
        lowest = stand
        for i in range(stand+1,len(l)):
            if l[i]<l[lowest]:
                lowest = i
        l[stand], l[lowest] = l[lowest], l[stand]
    
    return l

def quick_sort(l):
    
    if len(l)<2:
        return l
    pivot = l[0]

    left = [i for i in l[1:] if pivot>i]
    right = [i for i in l[1:] if pivot<=i]

    return quick_sort(left) + [pivot] + quick_sort(right)

a = [40, 1, 5, 74, 24, 56, 30, 99, 7]
print(selection_sort(a))
print(quick_sort(a))