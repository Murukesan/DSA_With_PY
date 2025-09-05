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
node4.next=node1

node4.prev=node3
node3.prev=node2
node2.prev=node1
node1.prev=node4

#Print forward

print("Linked list Forward order")
currentnode=node1
start=node1
count=0
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.next
    if currentnode==start:
        count += 1
        if count==2:
            break
        else:
            continue


print("...")

currentnode=node4
start=node4
count=0
print("Linked list Backward order")
while currentnode:
    print(currentnode.data,end="->")
    currentnode=currentnode.prev
    if currentnode==start:
        count += 1
        if count==2:
            break
        else:
            continue
print("...")