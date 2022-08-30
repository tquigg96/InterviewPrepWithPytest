class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def DFS(root): #do I need a visited?
    stack = [root]


    while len(stack) > 0:
        current = stack.pop()
        print(current.val)
        if(current.left):
            stack.append(current.left)
            
        if(current.right):
            stack.append(current.right)

def BFS(root):
    queue = [root]

    while(len(queue) > 0):
        current = queue.pop(0)
        print(current.val)

        if(current.left):
            queue.append(current.left)
        if (current.right):
            queue.append(current.right)


def find(root, target):
    stack = [root]
   

    while len(stack) > 0:
        current = stack.pop()
        if(current.val == target):
            return True
        

        if(current.left):
            stack.append(current.left)
            
        if(current.right):
            stack.append(current.right)
    return False
    
    

a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')

a.left = b
a.right = c
b.left = d
b.right = e

print("\nDepth First Search: \n" )
DFS(a)
print("\nBreadth First Search: \n")
BFS(a)
print("\nfind value using depth first \n")
check = find(a, 'e')
print(str(check) + "\n")

