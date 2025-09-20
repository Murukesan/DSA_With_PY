Queue=[]

#Enque
Queue.append('A')
Queue.append('B')
Queue.append('C')
print('Queue',Queue)
#Deque
element=Queue.pop(0)
print('Deque',element)
print('Queue',Queue)
#is Empty
isempty=not bool(Queue)
print('isEmpty',isempty)
#peek
peek=Queue[0]
print('Peek',peek)
#size
print('size',len(Queue))