class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0

    #enque
    def enque(self,data):
        Node=node(data)
        if self.rear is None:
            self.front=self.rear=Node
            self.size+=1
            return
        self.rear.next=Node
        self.rear=Node
        self.size+=1
    def Print(self):
        current=self.front
        while current:
            print(current.data,end='->')
            current=current.next
    #deque

    def deque(self):
        if self.isEmpty():
            return 'Queue is Empty'
        temp=self.front
        self.front=temp.next
        self.size-=1
        if self.front is None:
            self.rear = None
        return temp.data
    #isEmpty
    def isEmpty(self):
        return self.size==0
    #peek
    def peek(self):
        if self.isEmpty():
            return 'Queue is Empty'
        return self.front.data


queue=Queue()
queue.enque('A')
queue.enque('B')
queue.enque('C')
print(queue.Print())
print(queue.isEmpty())
print(queue.deque())
print(queue.Print())
print(queue.peek())
print(queue.Print())



