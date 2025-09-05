class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

node1=Node("Hello")
node2=Node(2)
node3=Node(3)
node4=Node(4)

node1.next=node2
node2.next=node3
node3.next=node4

node4.prev=node3
node3.prev=node2
node2.prev=node1

#Print forward

print("Linked list ascending order")
currentnode=node1
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
print("null")

currentnode=node4

print("Linked list descending order")
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.prev
print("null")