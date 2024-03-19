import sys
class Node(object):
    def __init__(self, n):
        self.name = n
        self.left =self.right = None

def first(fnode):
    print(fnode.name)
    if fnode.left != '.':
        first(fnode.left)
    if fnode.right != '.':
        first(fnode.right)


N = int(sys.stdin.readline())
tree = {}
temp = []
for _ in range(N):
    my, left, right = map(str,sys.stdin.readline().strip().split(' '))
    temp.append([my,left,right])
    Node(my,left,right)

root = Node(temp[0][0],temp[0][1],temp[0][2])
first(root)