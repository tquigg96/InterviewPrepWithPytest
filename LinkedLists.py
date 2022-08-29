
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
        return

    while(current != None):
        sum += current.val
        current = current.next
    
    print(sum)

def push(head,node): 

    
    if head == None :
        print("error no linked List")
        return

    if node == None:
        print("error no node to insert")
        return

    if head.next == None:
        head.next = node
        node.next = None
        return

    current = head
    while(current.next != None):
        current = current.next

    current.next = node
    node.next = None
    return

def pop(head):
    if head == None:
        return None


    value = head.val
    temp = head
    
    if temp != None:
        head = temp.next
        temp = None

    
    return value


    
 

a = singleNode(1)
b = singleNode(2)
c = singleNode(3)

push(a, b)
push(a, c)

printLinkedList(a)

value = pop(a)
print(value)
printLinkedList(a)
sumNodes(a)