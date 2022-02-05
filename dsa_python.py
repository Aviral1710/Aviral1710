##''' Singly Linked List '''
##
##class Node:
##    def __init__(self,data):
##        self.data = data
##        self.nextNode = None
##
##class LinkedList:
##    def __init__(self):
##        self.head = None
##        self.size = 0
##
##     # O(1)   
##    def insertStart(self,data):
##        self.size = self.size + 1
##        newNode = Node(data)
##
##        if not self.head:
##            self.head = newNode
##        else:
##            newNode.nextNode = self.head ## this is the previous head inserted
##            self.head = newNode
##
##    # O(1)
##    def size(self):
##        return self.size
##
##    def remove(self,data):
##
##        if self.head is None:
##            return
##
##        self.size = self.size-1
##
##        currentNode = self.head
##        previousNode = None
##
##        while currentNode.data != data:
##            previousNode =  currentNode
##            currentNode = currentNode.nextNode
##            
##        if previousNode is None: #means we want to remove starting node
##            self.head = currentNode.nextNode
##        else:
##            previousNode.nextNode = currentNode.nextNode #updating references
##            
##    # O(n) not good
##    def size2(self):
##        actualNode = self.head
##        size = 0
##
##        while actualNode is not None:
##            size += 1
##            actualNode = actualNode.nextNode
##
##        return size
##
##    # O(n)
##    def insertEnd(self,data):
##        self.size = self.size + 1
##        newNode = Node(data) ## creating new node
##        actualNode = self.head ## first node
##
##        while actualNode.nextNode is not None:
##            actualNode = actualNode.nextNode
##
##        actualNode.nextNode = newNode ## inserting newNode to its given position
##
##    def traverseList(self):
##        actualNode = self.head
##
##        while actualNode is not None:
##            print(actualNode.data)
##            actualNode = actualNode.nextNode
##
##ll = LinkedList()
##
##ll.insertStart(12)
##ll.insertStart(122)
##ll.insertStart(3)
##ll.insertEnd(31)
##
##ll.traverseList()
##
##ll.remove(12)
##ll.traverseList()


''' Doubly Linked List ''' 
class Node:
    def __init__(self,data):
        self.data = data
        self.previousNode = None
        self.nextNode = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self,data):
        
        newNode = Node(data)
        
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.nextNode = newNode
            newNode.previousNode = self.tail
            self.tail = newNode
        self.size += 1

    def pop(self):
        if not self.head:
            return 
        
        poppedNode = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.tail = poppedNode.previousNode
            self.tail.nextNode = None
            poppedNode.previousNode = None

        self.size -= 1
        return poppedNode.data

    def shift(self): ## deleting node from begining of dll
        if self.size == 0:
            return

        oldHead = self.head

        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.head = oldHead.nextNode
            self.head.previousNode = None
            oldHead.nextNode = None

        self.size -= 1
        return oldHead.data

    def unshift(self,data): ## insert node at begining of dll
        newNode = Node(data)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode

        else:
            self.head.previousNode = newNode
            newNode.nextNode = self.head
            self.head = newNode

        self.size += 1

    def get(self,index): ## accessing a node in a doubly Linked List by its position
        if index < 0 and index >= self.size:
            return
        else:
            count = 0
            current = self.head
            while count is not index:
                current = current.nextNode
                count += 1
                
        return current.data

    def set(self,index,val): ## update the value at an index
        self.val = val
        foundNode = self.get(index)

        if foundNode is not None:
            foundNode.val = val
            return true
        return false

        
    def traverseList(self):
        currentNode = self.head
        
        while currentNode is not None:
            print(f'{currentNode.data} ->', end=" ")
            currentNode = currentNode.nextNode
        

dll = DoublyLinkedList()
dll.insert(11)
dll.insert(99)
dll.insert(121)
dll.insert(100)
dll.insert(34)

dll.traverseList()

print("\n")
print(dll.pop())

dll.traverseList()
            
print("\n")
print(dll.shift())
dll.traverseList()

print("\n")

dll.unshift(20)
dll.unshift(30)

dll.traverseList()

print("\n")
print(dll.get(3))

dll.set(2,502)

dll.traverseList()
