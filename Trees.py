class node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    

a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')

a.left = b
a.right = c
b.left = d
b.right = e

