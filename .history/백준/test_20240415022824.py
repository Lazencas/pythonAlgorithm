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

def split(l):
    if len(l)<2:
        return l
    half = len(l)//2
    left =split([i for i in l[:half]]) 
    right=split([i for i in l[half:]])
    return merge(left,right)
    
def merge(left, right):
    merged = list()
    left_point, right_point = 0,0
    while len(left)>left_point and len(right)>right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point+=1
        else:
            merged.append(left[left_point])
            left_point+=1
    while len(left)>left_point:
        merged.append(left[left_point])
        left_point+=1
    while len(right)>right_point:
        merged.append(right[right_point])
        right_point+=1
    return merged

a = [40, 1, 5, 74, 24, 56, 30, 99, 7]
print(selection_sort(a))
print(quick_sort(a))
print(split(a))