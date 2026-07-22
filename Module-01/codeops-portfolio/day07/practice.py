# list index .... O(1) because item is accessed with index and the index let's us know the position directly
# single loop ... O(n) because it has to iterate each value of the list
#nested loop... O(n^2) because one loop runs n times, and inside it another loop runs n times.
#dict lookup ... O(1) because items are accessed with the key value it will directly access that key's value
#binary search ... O(log n) binary search be dividing the list in two then drops the other one it will be log n (shortly it halfs the list)

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        self.stack.remove(len(self.stack))

    def list_stack(self):
        for value in self.stack:
            print(value)
# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.pop()
# stack.pop()


# stack.list_stack()

# class Queue():
#     def __init__(self):
#         self.queue =[]
    
#     def enqueue(self, value):
#         self.queue.append(value)
    
#     def dequeue(self):
#         self.queue.remove(self.queue[0])
    
#     def list_queue(self):
#         for value in self.queue:
#             print(value)

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.dequeue()
# queue.dequeue()

# queue.list_queue()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
            
        current = self.head
        while current.next is not None:
            current = current.next
            
        current.next = new_node
    
    def print_all(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.print_all()