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
        return l[0]
    pivot = l[0]
    left, right = list(),list()
    for i in range(len(l)):
        if pivot>l[i]:
            left.append(l[i])
        else:
            right.append(l[i])

    return quick_sort(left) + [pivot] + quick_sort(right)

a = [40, 1, 5, 74, 24, 56, 30, 99, 7]
print(selection_sort(a))
print(quick_sort(a))