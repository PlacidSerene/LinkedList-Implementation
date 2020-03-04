# class myLinkedList:
#     def __init__(self):
#         head = {
#             value: 10,
#             next: {
#                 value: 5,
#                 next{
#                     value: 16,
#                     next: None
#                 }
#             }
#         }
class Node():

  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList():


    def __init__(self):
        self.head = None
        self.tail = None


  
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node 
            self.length += 1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        self.length += 1
    
    def printList(self):
        array = []
        currentNode = self.head
        while (currentNode != None):
            array.append(currentNode.data)
            currentNode = currentNode.next
        return array
    
    def insert(self, index, data):
        new_node = Node(7)
        if index == 0:
            self.prepend(data) 
            return self.printList()
        if index > self.length - 1:
            self.append(data) 
            return self.printList()
        before_node = self.traversaltoIndex(index-1)
        after_node = before_node.next
        before_node.next = new_node
        new_node.next = after_node
        self.length += 1 
    def traversaltoIndex(self,index):
        currentNode = self.head
        counter = 0
        while (counter != index):
            currentNode = currentNode.next
            counter += 1
        return currentNode
    def remove(self, index):
        before_node = self.traversaltoIndex(index-1)
        unwanted_node = before_node.next
        after_node = unwanted_node.next
        before_node.next = after_node
        self.length -=1


  

firstLinkedList = LinkedList()
firstLinkedList.append(15)
firstLinkedList.append(6)
firstLinkedList.append(10)
firstLinkedList.append(8)
firstLinkedList.remove(2)
print(firstLinkedList.printList())


