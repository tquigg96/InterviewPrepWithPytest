
class singleNode:
    def __init__(self, val):
        self.next = None
        self.val = val


def printLinkedList(head):
    current = head
    
    while(current != None):
        print(current.val)
        current = current.next

def sumNodes(head):
    current = head
    sum = 0

    if head == None:
        print("error no LinkedList created")

    while(current != None):
        sum += current.val
        current = current.next
    
    print(sum)

def insertNode(pos, head):
    current = head

a = singleNode(1)
b = singleNode(2)
c = singleNode(3)

a.next = b
b.next = c

printLinkedList(a)
sumNodes(a)