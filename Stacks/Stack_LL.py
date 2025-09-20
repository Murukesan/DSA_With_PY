

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None
        self.size=0
#push
    def push(self,value):
        new_node=Node(value)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size+=1
#pop
    def pop(self):
        if self.size == 0:
            return "Stack is empty"
        popped_node=self.head
        self.head=self.head.next
        self.size-=1
        return popped_node.data
#peek
    def peek(self):
        if self.size==0:
            return "Stack is empty"
        return self.head.data
#is_Empty
    def is_empty(self):
        if self.size==0:
            return "Stack is Empty"
        else:
            return "Stack is not Empty"
#print
    def print(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
mystack=Stack()
print(mystack.is_empty())
mystack.push(3)
mystack.push(2)
mystack.push(1)
print(mystack.print())
print('Peek: ',mystack.peek())
print('Pop: ',mystack.pop())
print(mystack.print())
print(mystack.is_empty())

