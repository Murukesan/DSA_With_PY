#Node Creation
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Traversal
def print_traversal(head):
    current=head
    while current:
        print(current.data,end='->')
        current=current.next

    print('null')
# Remove a node
def remove(ntd,head):
    if ntd==head:
        return head.next
    current=head
    while current.next and current.next!=ntd:
        current=current.next
    if current.next is None:
        return head
    current.next=current.next.next
    return head

# find lowest
def lowest(head):
    current=head
    min=current.data
    while current:
        if min>current.data:
            min=current.data
            current=current.next
        else:
            current=current.next
    return min
# find highest
def highest(head):
    current=head
    max=current.data
    while current:
        if max<current.data:
            max=current.data
            current=current.next
        else:
            current=current.next
    return max
# Insert a node
def insert(head,Newnode,place):
    if place==1:
        Newnode.next=head
        return Newnode
    current=head
    print(current.data)
    for i in range(place-2):
        if current is None:
            break
        current=current.next
    print(current.data)
    Newnode.next=current.next
    current.next=Newnode
    return head
# Sort

#Linked list node assign

node1=Node(7)
node2=Node(5)
node3=Node(3)
node4=Node(1)

node1.next=node2
node2.next=node3
node3.next=node4

print("Before Deletion:")
print_traversal(node1)
remove(node4,node1)
print("After Deletion:")
print_traversal(node1)
print("Minimum node:")
print(lowest(node1))
print("Maximum node:")
print(highest(node1))
print("Before insertion: ")
print_traversal(node1)
Newnode=Node(1)
insert(node1,Newnode,2)
print("After Insertion: ")
print_traversal(node1)


